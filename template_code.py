from fastapi import FastAPI
from typing import List, Dict

TEMPLATES = [
    {
        "min_age": 18,
        "max_age": 99,
        "country": "US",
        "audience_attributes": ["gender", "race", "origin"]
    },
    {
        "min_age": 16,
        "max_age": 120,
        "country": "CA",
        "audience_attributes": ["gender", "region"]
    }
]

ATTRIBUTE_VALUES = [
    {
        "Country": "US",
        "Parent Attribute Name": "gender",
        "Audience Attribute Value": "Male",
        "Audience Attribute Label": "Male",
        "Audience Attribute Description": None
    },
    {
        "Country": "US",
        "Parent Attribute Name": "gender",
        "Audience Attribute Value": "Female",
        "Audience Attribute Label": "Female",
        "Audience Attribute Description": None
    },
    {
        "Country": "US",
        "Parent Attribute Name": "race",
        "Audience Attribute Value": "AA",
        "Audience Attribute Label": "African American",
        "Audience Attribute Description": None
    },
    {
        "Country": "US",
        "Parent Attribute Name": "race",
        "Audience Attribute Value": "HA",
        "Audience Attribute Label": "Hispanic American",
        "Audience Attribute Description": None
    },
    {
        "Country": "US",
        "Parent Attribute Name": "origin",
        "Audience Attribute Value": "unknown",
        "Audience Attribute Label": "Origin",
        "Audience Attribute Description": None
    },
    {
        "Country": "CA",
        "Parent Attribute Name": "gender",
        "Audience Attribute Value": "m",
        "Audience Attribute Label": "Male",
        "Audience Attribute Description": None
    },
    {
        "Country": "CA",
        "Parent Attribute Name": "gender",
        "Audience Attribute Value": "f",
        "Audience Attribute Label": "Female",
        "Audience Attribute Description": None
    },
    {
        "Country": "CA",
        "Parent Attribute Name": "region",
        "Audience Attribute Value": "national",
        "Audience Attribute Label": "English Speaking Regions",
        "Audience Attribute Description": None
    },
    {
        "Country": "CA",
        "Parent Attribute Name": "region",
        "Audience Attribute Value": "quebec",
        "Audience Attribute Label": "French Speaking Regions",
        "Audience Attribute Description": None
    }
]
app = FastAPI()

@app.get("/audiences")
async def get_audiences(country: str):
    response = {}

    for template in TEMPLATES:
        if template["country"] == country:
            response["min_age"] = template["min_age"]
            response["max_age"] = template["max_age"]
            response["country"] = template["country"]
            response["audience_attributes"] = {}

            for attribute in template["audience_attributes"]:
                attribute_values = []
                for attr_value in ATTRIBUTE_VALUES:
                    if (
                        attr_value["Country"] == country
                        and attr_value["Parent Attribute Name"] == attribute
                    ):
                        attribute_values.append(
                            {
                                "attribute_value": attr_value["Audience Attribute Value"],
                                "label": attr_value["Audience Attribute Label"],
                            }
                        )

                response["audience_attributes"][attribute] = attribute_values

            break

    return response


