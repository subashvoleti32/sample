#!/bin/bash

gcloud config configurations create emulator
gcloud config set auth/disable_credentials true
gcloud config set project ${PROJECT_ID} --quiet
gcloud config set api_endpoint_overrides/spanner http://localhost:9020/
gcloud spanner instances create ${INSTANCE_ID}  --config=emulator-config --description="demo" --nodes=1
gcloud spanner databases create ${DATABASE_ID} --instance=${INSTANCE_ID}
gcloud spanner databases create test-database --instance test2-instance --ddl "CREATE TABLE attribute_country (country_uuid STRING(36), country_name STRING(200)) PRIMARY KEY (country_uuid)"

gcloud spanner databases ddl update test-database --instance=test2-instance --ddl "CREATE TABLE attributes_label (uuid STRING(36), country_uuid STRING(36), attribute_name STRING(250),label STRING(306),description STRING(250)) PRIMARY KEY (uuid)"
gcloud spanner databases ddl update test-database --instance=test2-instance --ddl="ALTER TABLE attributes_label ADD CONSTRAINT attributes_label_uuid_fk FOREIGN KEY (country_uuid) REFERENCES attribute_country (country_uuid)"

 
gcloud spanner databases ddl update test-database --instance=test2-instance --ddl "CREATE TABLE attributes_name (uuid STRING(36), country_uuid STRING(36), attribute_name STRING(250)) PRIMARY KEY (uuid)"
gcloud spanner databases ddl update test-database --instance=test2-instance --ddl="ALTER TABLE attributes_name ADD CONSTRAINT attributes_name_uuid_fk FOREIGN KEY (country_uuid) REFERENCES attribute_country (country_uuid)"

python inserting_data_emulator.py 



import uuid 
from google.cloud import spanner
import uuid

client = spanner.Client()
database = client.instance("test2-instance").database("test-database")

def insert_country_values(transaction,country_attribute):
    row_ct = transaction.execute_update(
        "INSERT INTO attribute_country (country_uuid,country_name) VALUES "
        f"('{country_attribute['country_uuid']}', '{country_attribute['country_name']}')"
    )
country_attribute = {"country_uuid":'CA','country_name':'CANADA'}
country_attribute1 = {"country_uuid":'US','country_name':'USA'}



database.run_in_transaction(insert_country_values,country_attribute)
database.run_in_transaction(insert_country_values,country_attribute1)



def insert_attributes_name(transaction,attribute_names):
    attribute_id = uuid.uuid4()
    row_ct = transaction.execute_update(
        "INSERT INTO attributes_name (uuid,country_uuid,attribute_name) VALUES "
        f"('{attribute_id}', '{attribute_names['country_uuid']}','{attribute_names['attribute_name']}')"
    )

attribute_name = {"country_uuid":'CA','country_name':'CANADA','attribute_name':'Gender'}
attribute_name1 = {"country_uuid":'US','country_name':'USA','attribute_name':'Gender'}
attribute_name2 = {"country_uuid":'CA','country_name':'CANADA','attribute_name':'Age'}
attribute_name3 = {"country_uuid":'US','country_name':'USA','attribute_name':'Age'}
database.run_in_transaction(insert_attributes_name,attribute_name)
database.run_in_transaction(insert_attributes_name,attribute_name1)
database.run_in_transaction(insert_attributes_name,attribute_name2)
database.run_in_transaction(insert_attributes_name,attribute_name3)
def insert_attributes_label(transaction,attribute_names):
    attribute_id = uuid.uuid4()
    row_ct = transaction.execute_update(
        "INSERT INTO attributes_label (uuid,country_uuid,attribute_name,label,description) VALUES "
        f"('{attribute_id}', '{attribute_names['country_uuid']}','{attribute_names['attribute_name']}','{attribute_names['label']}','{attribute_names['description']}')"
    )
attribute_label = {"country_uuid":'US','attribute_name':'Gender','label':'Gender','description':'The Gender of  Audience'}
attribute_label1 = {"country_uuid":'US','attribute_name':'Age','label':'Age','description':'The Age of  Audience'}
attribute_label2 = {"country_uuid":'CA','attribute_name':'Gender','label':'Gender','description':'The Gender of  Audience'}
attribute_label3 = {"country_uuid":'CA','attribute_name':'Age','label':'Age','description':'The Age of  Audience'}
database.run_in_transaction(insert_attributes_label,attribute_label)
database.run_in_transaction(insert_attributes_label,attribute_label1)
database.run_in_transaction(insert_attributes_label,attribute_label2)
database.run_in_transaction(insert_attributes_label,attribute_label3)
