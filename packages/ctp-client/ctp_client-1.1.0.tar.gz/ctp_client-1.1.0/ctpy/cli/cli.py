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


import socket
import logging
from pathlib import Path

import click
import tabulate
from click_loglevel import LogLevel
import yaml
from yaml.loader import SafeLoader

from ctpy import CTPYclient
from ctpy import exceptions
from ctpy.helpers import poll_object_tracker_for_studyuid, summarize_object_tracker_content, UserRoles, User, hash_password, users_to_xml

@click.group()
@click.version_option()
@click.option('--loglevel', type=LogLevel(), default=logging.INFO)
def cli(loglevel):
    logging.basicConfig(
        format=f"%(asctime)s - {socket.gethostname()} - [%(levelname)-8s] %(message)s",
        level=loglevel,
    )

@cli.command()
@click.option('--lookup-table-filename', type=Path, required=True)
@click.option('--server', required=True)
@click.option('--dicom-anonymizer-id', required=True)
@click.option('--username', required=True)
@click.option('--password', required=True, prompt=True, hide_input=True)
def post_lookup_table(lookup_table_filename, server,
                        dicom_anonymizer_id, username, password):
    ctpy_client = CTPYclient(server, username, password, rate_limit=0.2)
    with open(lookup_table_filename, encoding='utf-8') as lookup_table_file:
        lut = yaml.load(lookup_table_file, Loader=SafeLoader)
        for key, value in lut.items():
            try:
                ctpy_client.add_to_lookup(dicom_anonymizer_id, key, value)
            except exceptions.CTPYFailedAddingLUT:
                pass
            break

@cli.command()
@click.option('--server', required=True)
@click.option('--pipeline-id', type=int, default=0, required=True)
@click.option('--object-tracker-id', type=int, default=1, required=True)
@click.option('--username', required=True, default="king")
@click.option('--password', required=True, default="password", prompt=True, hide_input=True)
@click.option('--patient-id', required=True)
@click.option('--study-uid', 'study_uid_filter')
@click.option('--delay', type=int, default=5)
@click.option('--timeout', type=int, default=900)
def check_object_tracker(server, pipeline_id, object_tracker_id,
                         username, password, patient_id, study_uid_filter, delay,
                         timeout):
    ctpy_client = CTPYclient(server, username, password, rate_limit=0.2)
    object_tracker_data = poll_object_tracker_for_studyuid(ctpy_client,
                                                           pipeline_id,
                                                           object_tracker_id,
                                                           patient_id,
                                                           study_uid_filter,
                                                           delay,
                                                           timeout)
    logging.debug('patient_data: %s', object_tracker_data)
    if object_tracker_data and patient_id in object_tracker_data:
        for study_uid, series_info in object_tracker_data[patient_id].items():
            for series_uid, instances in series_info.items():
                logging.info('%s|%s|%s', study_uid, series_uid, instances)

@cli.command()
@click.option('--server', required=True)
@click.option('--pipeline-id', type=int, default=0, required=True)
@click.option('--idmap-id', type=int, default=1, required=True)
@click.option('--username', required=True, default="king")
@click.option('--password', required=True, default="password", prompt=True, hide_input=True)
@click.option('--keytype', required=True)
@click.option('--key', required=True)
def query_idmap(server, pipeline_id, idmap_id, keytype, key,
                username, password):
    ctpy_client = CTPYclient(server, username, password, rate_limit=0.2)
    study_uid = ctpy_client.idmap_search(pipeline_id, idmap_id, key, keytype)
    if study_uid:
        logging.info(study_uid)


@cli.command()
@click.option('--server', required=True)
@click.option('--username', required=False)
@click.option('--password', required=False)
def get_summary(server, username, password):
    ctpy_client = CTPYclient(server, username, password, rate_limit=0.2)
    summary = ctpy_client.get_ctp_summary()
    logging.info(f"\n{tabulate.tabulate([s.to_table_row() for s in summary], headers=['pipeline', 'import', 'export', 'quarantines'])}")


@cli.command()
@click.option('--server', required=True)
@click.option('--username', required=True)
@click.option('--password', required=True)
@click.option('--pipeline-name', required=True)
def get_tracker_summary(server, username, password, pipeline_name):
    ctpy_client = CTPYclient(server, username, password, rate_limit=0.2)
    pipeline = ctpy_client.server.pipelines.get(pipeline_name)
    if pipeline is None:
        raise exceptions.CTPYPipelineNotFound(f"Pipeline {pipeline_name} not found!")
    
    trackers_summary = list()
    object_trackers = ctpy_client.find_object_tracker_stages(pipeline)
    for tracker_id, object_tracker in object_trackers:
        object_tracker_contents = ctpy_client.get_object_tracker_patient_info(pipeline_id=pipeline.pipeline_id, stage_id=tracker_id)
                
        trackers_summary.append([object_tracker.name, *summarize_object_tracker_content(object_tracker_contents)])
    logging.info(f"\n{tabulate.tabulate(trackers_summary, headers=['name', 'subjects', 'experiments', 'scans', 'instances'])}")


@cli.command()
@click.option('--server', required=True)
@click.option('--username', required=True)
@click.option('--password', required=True)
@click.option('--update-user', required=True)
@click.option('--update-password', required=True)
def update_password(server, username, password, update_user, update_password):
    ctpy_client = CTPYclient(server, username, password)
    ctpy_client.get_users()

    # Fetch users 
    users = ctpy_client.get_users()   
    for user in users:
        if user.name == update_user:
            user.password = update_password
            break
    else:
        logging.info(f"User '{user}'' not found")
        return
    
    ctpy_client.update_password(users)


@cli.command()
@click.option('--server', required=True)
@click.option('--username', required=True)
@click.option('--password', required=True)
def get_users(server, username, password):
    ctpy_client = CTPYclient(server, username, password)
    users = ctpy_client.get_users()
    tabular_data = []
    for user in users:
        user_data = [user.name] + ['X' if role in user.roles else '' for role in UserRoles]
        tabular_data.append(user_data)

    logging.info(f"\n{tabulate.tabulate(tabular_data, headers=['name'] + [role.name for role in UserRoles] )}")


@cli.command()
@click.option('--user', '-u', 'users_str', multiple=True, required=True)
def create_users_xml(users_str):
    users = []
    for user_str in users_str:
        username, password = user_str.split(',')[0:2]
        roles = user_str.split(',')[2:]
        roles = [UserRoles[role] for role in roles]
        user = User(username, roles)
        user.password = password
        users.append(user)
    print(users_to_xml(users))
    


