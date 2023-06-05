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

        for row in results:
            print(row)
