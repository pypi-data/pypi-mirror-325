# Copyright 2017 Biomedical Imaging Group Rotterdam, Departments of
# Medical Informatics and Radiology, Erasmus MC, Rotterdam, The Netherlands

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from time import sleep, time
import logging
import datetime
from typing import Dict, List, Optional, Union
from enum import Enum
import hashlib

import bs4
from pydantic import BaseModel, Field, AliasChoices, field_validator


def parse_object_tracker_results(object_tracker_string: str,
                                 patient_id_filter: Optional[str] = None,
                                 study_uid_filter: Optional[str] = None) -> Union[None, Dict[str, Dict[str, Dict[str, str]]]]:
    try:
        data = object_tracker_string.split()[1:]
    except IndexError:
        return None
    object_tracker_dict = {}
    for row in data:
        row = row.split(',')
        patient_id = row[0]
        study_uid = row[1]
        series_uid = row[2]
        instances = int(row[3])
        if patient_id_filter and not patient_id == patient_id_filter:
            logging.debug('Filtering Patient: %s not equal: %s', patient_id, patient_id_filter)
            continue
        if study_uid_filter and not study_uid == study_uid_filter:
            logging.debug('Filtering StudyUID: %s', study_uid, study_uid_filter)
            continue
        if patient_id in object_tracker_dict:
            if study_uid in object_tracker_dict[patient_id]:
                if series_uid in object_tracker_dict[patient_id][study_uid]:
                    object_tracker_dict[patient_id][study_uid][series_uid] = instances
                    logging.debug('Update %s to object_tracker_dict', instances)
                else:
                    object_tracker_dict[patient_id][study_uid][series_uid] = instances
                    logging.debug('Add %s to object_tracker_dict', instances)
            else:
                object_tracker_dict[patient_id][study_uid] = {series_uid: instances}
                logging.debug('Add %s|%s;%s to object_tracker_dict',
                                study_uid, series_uid, instances)
        else:
            logging.debug('Add %s|%s|%s;%s to object_tracker_dict',
                            patient_id, study_uid, series_uid, instances)
            object_tracker_dict[patient_id] = {study_uid: {series_uid: instances}}
    return object_tracker_dict


def parse_idmap_results(idmap_string: str) -> Union[None, str]:
    logging.debug(f'idmap: {idmap_string}')
    lines = idmap_string.split('\n')
    _, new = lines[1].split(',')

    if new.startswith('=("'):
        trial_uid = new[3:-2]
        return trial_uid
    return None


def poll_object_tracker_for_studyuid(ctpy_session, pipeline_id,
                                     object_tracker_id, patient_id,
                                     study_uid, delay, timeout):
    old_data = object_tracker_data = {}
    last_update = int(time())
    logging.debug(f'Querying for patient:{patient_id}, study_uid: {study_uid}')
    while old_data == object_tracker_data:
        object_tracker_data = ctpy_session.get_object_tracker_patient_info(pipeline_id,
                                                                           object_tracker_id,
                                                                           '',
                                                                           patient_id,
                                                                           study_uid)
        logging.debug('Checking for new data...')
        if old_data == object_tracker_data:
            logging.debug('No incoming data check timeout')
            if int(time() - last_update) > timeout:
                logging.debug('Timeout reached')
                break
        else:
            last_update = int(time())
            logging.debug('Incoming data...')
            logging.debug(f'Found: {object_tracker_data}')

        old_data = object_tracker_data
        sleep(delay)

    return object_tracker_data


class CtpSummary(BaseModel):
    pipeline: str = Field('', validation_alias=AliasChoices('Pipeline'))
    import_queues: int = Field(0, validation_alias=AliasChoices('ImportQueues'))
    export_queues: int = Field(0, validation_alias=AliasChoices('ExportQueues'))
    quarantines: int = Field(0, validation_alias=AliasChoices('Quarantines'))
    time_stamp: datetime.datetime = Field(
        default_factory=lambda: datetime.datetime.now())  # pylint:disable=unnecessary-lambda

    def __init__(self, row):
        super().__init__()
        values = row.find_all('td')
        self.pipeline = values[0].text
        self.import_queues = int(values[1].text)
        self.export_queues = int(values[2].text)
        self.quarantines = int(values[3].text)

    @field_validator('import_queues', 'export_queues', 'quarantines', mode='before')
    @classmethod
    def remove_separators(cls, v: str) -> int:
        if isinstance(v, int):
            return v
        return int(v.replace(',', ''))
    
    def to_table_row(self) -> List:
        return [self.pipeline, self.import_queues, self.export_queues, self.quarantines]


def parse_summary(html: Union[str, bytes]) -> Union[None, List[CtpSummary]]:
    soup = bs4.BeautifulSoup(html, 'html.parser')
    tables = soup.find_all('table', attrs={'class': 'summary'})
    if len(tables) != 1:
        return None

    rows = tables[0].find_all('tr')
    results = [CtpSummary(row) for row in rows[1:]]

    return results


def parse_step(html: Union[str, bytes]) -> Dict[str, Dict[str, str]]:
    soup = bs4.BeautifulSoup(html, 'html.parser')

    status_table = soup.find('h2', string='Status').find_next_sibling('table')
    config_table = soup.find('h2', string='Configuration').find_next_sibling('table')

    return {
        'status': parse_vertical_table(status_table),
        'config': parse_vertical_table(config_table),
    }


def parse_vertical_table(table_element: bs4.Tag) -> Dict[str, str]:
    """
    Parse the vertical tables that just have 2 columns with a key-value structure

    :param table_element: table DOM element
    :return: table parsed into a dict
    """
    rows = table_element.find_all('tr')

    result = {}
    for row in rows:
        elements = row.find_all('td')
        if len(elements) != 2:
            raise ValueError('Expected table to have 2 columns only!')

        result[elements[0].text] = elements[1].text

    return result


def summarize_object_tracker_content(object_tracker_content):
    subjects = 0
    experiments = 0
    scans = 0
    instances = 0
    for _, subject_info in object_tracker_content.items():
        subjects += 1
        for _, experiment_info in subject_info.items():
            experiments += 1
            for _, scan_instances in experiment_info.items():
                scans += 1
                instances += scan_instances

    return subjects, experiments, scans, instances


UserRoles = Enum('UserRoles', [('admin', 0), ('audit', 1), ('delete', 2), ('export', 3), ('guest', 4), ('import', 5), ('proxy', 6), ('qadmin', 7), ('read', 8), ('shutdown', 9)])


class User:
    """
    CTP user object
    """
    def __init__(self, username, roles:List[UserRoles]):
        self.name = username
        self.roles = roles
        self.password = ""

    def xml_entry(self):
        lines = []
        lines.append('    <user')
        lines.append(f'        password="{hash_password(self.password)}"')
        lines.append(f'        username="{self.name}">')
        for role in self.roles:
            lines.append(f'        <role>{role.name}</role>')
        lines.append('    </user>')
        return lines



def create_user_post(users: List[User]) -> Dict[str, str]:
    """
    Create POST data from list of users. based on the form of the UserManagerServlet.
    """
    data = {
        'suppress': ""
    }
    for i, role in enumerate(UserRoles):
        data[f'r{i}'] = role.name
    
    for i, user in enumerate(users):
        data[f'u{i}']  = user.name
        for role in user.roles:
            data[f'cbu{i}r{role.value}'] = 'on'
        data[f'p{i}'] = user.password
    return data


def parse_user_row(user_row):
    # Check of row is user or an empty row in the form.
    columns = user_row.find_all('td')
    username_input = columns[0].find('input')
    if username_input and 'value' in username_input.attrs:
        username = username_input['value']
    else:
        username = ""  # Default to empty if no username is found
        return None
    user_roles = []

    # Check the checkboxes for roles and add the role to the list if checked
    for i, role in enumerate(UserRoles):
        checkbox = columns[i+1].find('input')  # Skip first column (username)
        if checkbox and checkbox.get('checked') == 'true':
            user_roles.append(role)
    
    # Create a User object and append it to the list
    user = User(username, user_roles)
    return user

def parse_user_manager(html: Union[str, bytes]) -> List[User]:
    """
    Parses the table of the UserManagerServlet into a list of users
    """
    soup = bs4.BeautifulSoup(html, 'html.parser')
    tables = soup.find_all('table', attrs={'id': 'userTable'})
    if len(tables) != 1:
        return None
    rows = soup.select('table#userTable tr')[1:]
    
    users = []
    for row in rows:
        user = parse_user_row(row)
        if not user:
            continue
        users.append(user)

    return users


def hash_password(input_string, maxlen=None):
    """
    Hashes the input_string (password) using md5 sum and converting the hex string to a
    decimal. This is the method used by CTP in it's util library.
    """
    # Handle null input by setting it to "null"
    if input_string is None:
        input_string = "null"

    # Handle maxlen < 1 by setting it to a very large number (no limit)
    if not maxlen or maxlen < 1:
        maxlen = 2147483647  # A large value, equivalent to Integer.MAX_VALUE in Java
    
    md5_hash = hashlib.md5(input_string.encode('utf-8')).hexdigest()

    # Convert the MD5 hash (hex) to a decimal string and use maxlen to truncate.
    decimal_value = int(md5_hash, 16)
    return str(decimal_value)[:maxlen]

def users_to_xml(users):
    lines = []
    # Print users.xml
    lines.append('<users mode="digest">')
    for user in users:
        lines += user.xml_entry()
    lines.append('</users>')
    return '\n'.join(lines)