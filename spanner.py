import uuid
from fastapi import FastAPI
from google.cloud import spanner
from pydantic import BaseModel


app = FastAPI()


@app.get("/attributes/{country}")
def get_attribute_by_country(country:str):
    res=query_data("test2-instance","test7-database",country)
    return {"Values are successuflly retrieved"}


def query_data(instance_id, database_id,country):
    """Queries sample data from the database using SQL."""
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)
    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT *FROM Audience_Attributes WHERE country = @country_name",
            params= {"country_name":country},
            param_types={"country_name":spanner.param_types.STRING}
        )
        

 operation = database.update_ddl(["CREATE TABLE Audience_Attributes (id STRING(36), country STRING(2), name STRING(250), label STRING(250), description STRING(500)) PRIMARY KEY (id)"])
# operation.result()
# operation2 = database.update_ddl(["CREATE TABLE Audience_Attribute_Values (id STRING(36), attribute_id STRING(36), value STRING(250), label STRING(250), description STRING(500)) PRIMARY KEY (id)"])
# operation2.result()
# operation3 = database.update_ddl(["ALTER TABLE Audience_Attribute_Values ADD CONSTRAINT Audience_Attribute_Values_attribute_id_fk FOREIGN KEY (attribute_id) REFERENCES Audience_Attributes (id)"])
# operation3.result()

        for row in results:
            print(row)

            
            from google.cloud import spanner
import uuid

client = spanner.Client()
database = client.instance("test2-instance").database("test7-database")

# operation = database.update_ddl(["CREATE TABLE Audience_Attributes (id STRING(36), country STRING(2), name STRING(250), label STRING(250), description STRING(500)) PRIMARY KEY (id)"])
# operation.result()
# operation2 = database.update_ddl(["CREATE TABLE Audience_Attribute_Values (id STRING(36), attribute_id STRING(36), value STRING(250), label STRING(250), description STRING(500)) PRIMARY KEY (id)"])
# operation2.result()
# operation3 = database.update_ddl(["ALTER TABLE Audience_Attribute_Values ADD CONSTRAINT Audience_Attribute_Values_attribute_id_fk FOREIGN KEY (attribute_id) REFERENCES Audience_Attributes (id)"])
# operation3.result()

def insert_attributes(transaction, attribute, attribute_values):
    attribute_id = uuid.uuid4()
    row_ct = transaction.execute_update(
        "INSERT INTO Audience_Attributes (id, country, name, label, description) VALUES "
        f"('{attribute_id}', '{attribute['country']}', '{attribute['name']}', '{attribute['label']}', '{attribute['description']}')"
    )
    print("{} record(s) inserted.".format(row_ct))
    for attribute_value in attribute_values:
        value_row_ct = transaction.execute_update(
            "INSERT INTO Audience_Attribute_Values (id, attribute_id, value, label, description) VALUES "
            f"('{uuid.uuid4()}', '{attribute_id}', '{attribute_value['value']}', '{attribute_value['label']}', '{attribute_value['description']}')"
        )
        print("{} record(s) inserted.".format(value_row_ct))

gender_attribute = {"country":'US', "name":'gender', "label":'Gender', "description":'The gender of the audience members'}
gender_attribute_values = [
    {"value":'f', "label":'Female', "description":'Female'},
    {"value":'m', "label":'Male', "description":'Male'}
]
age_attribute = {"country":'US', "name":'age', "label":'Age', "description":'The age range of audience members'}
age_attribute_values = [
    {"value":'18+', "label":'18+', "description":'Greater than 18 years'},
    {"value":'36-42', "label":'36 to 42', "description":'36 to 42 years old'}
]
race_attribute={"country":"CA","name":"race","label":"race","description":"Thre description of race"}

race_attribute_values = [
    {"value":"03","label":"03","description":"Black"},
    {"value":"04","label":"04","description":"Asian/Pacific"}
]

occupation_attribute={"country":"CA","name":"HouseHold","label":"HouseHold","description":"The HouseHold Description"}
occupation_attribute_values = [
    {"value":"1","label":"1","description":"Professional"},
    {"value":"2","label":"2","description":"clerical"}
]

# database.run_in_transaction(insert_attributes, gender_attribute, gender_attribute_values)
# database.run_in_transaction(insert_attributes, age_attribute, age_attribute_values)

database.run_in_transaction(insert_attributes, occupation_attribute,occupation_attribute_values)
