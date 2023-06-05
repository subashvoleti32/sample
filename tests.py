def test_get_attribute_by_country_invalid_param():
    response = client.get("/attributes/123")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["path", "country"],
                "msg": "value is not a valid string",
                "type": "type_error.str"
            }
        ]
    }
    
def test_get_attribute_by_country_missing_param():
    response = client.get("/attributes/")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["path", "country"],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }
 
def test_get_attribute_by_country_internal_error(monkeypatch):
    def mock_query_data(instance_id, database_id, country):
        raise Exception("Database connection error")
    
    monkeypatch.setattr("main.query_data", mock_query_data)
    
    response = client.get("/attributes/US")
    assert response.status_code == 500
    assert response.json() == {"detail": "Internal server error"}
    
  
 
def test_insert_attributes():
    response = client.post("/attributes", json={
        "attribute": {
            "country": "US",
            "name": "test_attribute",
            "label": "Test Attribute",
            "description": "Test attribute description"
        },
        "attribute_values": [
            {
                "value": "1",
                "label": "Value 1",
                "description": "Value 1 description"
            },
            {
                "value": "2",
                "label": "Value 2",
                "description": "Value 2 description"
            }
        ]
    })
    assert response.status_code == 201
    assert response.json() == {"message": "Attributes inserted successfully"}
    
      
   Sure! Here are 10 test case scenarios for the provided code using FastAPI TestClient and pytest:

```python
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.mark.parametrize("country", ["US", "CA"])
def test_get_attribute_by_country_success(country):
    response = client.get(f"/attributes/{country}")
    assert response.status_code == 200
    assert response.json() == {"Values are successfully retrieved"}

@pytest.mark.parametrize("country", ["UK", "AU"])
def test_get_attribute_by_country_not_found(country):
    response = client.get(f"/attributes/{country}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Country not found"}

def test_get_attribute_by_country_invalid_param():
    response = client.get("/attributes/123")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["path", "country"],
                "msg": "value is not a valid string",
                "type": "type_error.str"
            }
        ]
    }

def test_get_attribute_by_country_missing_param():
    response = client.get("/attributes/")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["path", "country"],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }

def test_get_attribute_by_country_internal_error(monkeypatch):
    def mock_query_data(instance_id, database_id, country):
        raise Exception("Database connection error")
    
    monkeypatch.setattr("main.query_data", mock_query_data)
    
    response = client.get("/attributes/US")
    assert response.status_code == 500
    assert response.json() == {"detail": "Internal server error"}

def test_insert_attributes():
    response = client.post("/attributes", json={
        "attribute": {
            "country": "US",
            "name": "test_attribute",
            "label": "Test Attribute",
            "description": "Test attribute description"
        },
        "attribute_values": [
            {
                "value": "1",
                "label": "Value 1",
                "description": "Value 1 description"
            },
            {
                "value": "2",
                "label": "Value 2",
                "description": "Value 2 description"
            }
        ]
    })
    assert response.status_code == 201
    assert response.json() == {"message": "Attributes inserted successfully"}

def test_insert_attributes_invalid_body():
    response = client.post("/attributes", json={
        "invalid_key": "value"
    })
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body"],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }

def test_insert_attributes_invalid_attribute_values():
    response = client.post("/attributes", json={
        "attribute": {
            "country": "US",
            "name": "test_attribute",
            "label": "Test Attribute",
            "description": "Test attribute description"
        },
        "attribute_values": "invalid_value"
    })
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "attribute_values"],
                "msg": "value is not a valid list",
                "type": "type_error.list"
            }
        ]
    }

def test_insert_attributes_invalid_attribute_values():
    response = client.post("/attributes", json={
        "attribute": {
            "country": "US",
            "name": "test_attribute",
            "label": "Test Attribute",
            "description": "Test attribute description"
        },
        "attribute_values": "invalid_value"
    })
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "attribute_values"],
                "msg": "value is not a valid list",
                "type": "type_error.list"
            }
        ]
    }
    
   
