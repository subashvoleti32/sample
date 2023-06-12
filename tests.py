[
  [
    "5cd453b7-e7b0-4edf-a904-cd67fe50bde9",
    "US",
    "Age",
    "Age",
    "The Age of  Audience"
  ],
  [
    "0cdd1665-2f93-478f-9e03-ac56799892f8",
    "US",
    "Gender",
    "Gender",
    "The Gender of  Audience"
  ]
]




[['44acf2d7-3c0c-4751-b172-2bbb40b2191d', 'CA', 'Gender'], ['5b0bb06f-b837-4711-bcdd-be7a7b01b719', 'CA', 'Age'], ['90650d42-3bb0-4707-b393-a46df3ee1503', 'US', 'Gender'], ['114d5d90-8155-4c4d-95ce-3cdc155493cb', 'US', 'Age']]

[['114d5d90-8155-4c4d-95ce-3cdc155493cb', 'US', 'Age'], ['5b0bb06f-b837-4711-bcdd-be7a7b01b719', 'CA', 'Age'], ['44acf2d7-3c0c-4751-b172-2bbb40b2191d', 'CA', 'Gender'], ['90650d42-3bb0-4707-b393-a46df3ee1503', 'US', 'Gender']]



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
    
    
    
    def test_query_data():
    # Create a mock Spanner client and instance
    mock_spanner_client = Mock(spec=spanner.Client)
    mock_instance = Mock(spec=spanner.Instance)
    mock_database = Mock(spec=spanner.Database)

    # Patch the spanner.Client and spanner.Client.instance methods to return the mock objects
    with patch("main.spanner.Client", return_value=mock_spanner_client):
        with patch.object(mock_spanner_client, "instance", return_value=mock_instance):
            with patch.object(mock_instance, "database", return_value=mock_database):
                # Create a mock snapshot and mock results
                mock_snapshot = Mock()
                mock_results = Mock()
                mock_snapshot.execute_sql.return_value = mock_results

                # Patch the database.snapshot method to return the mock snapshot
                with patch.object(mock_database, "snapshot", return_value=mock_snapshot):
                    # Call the query_data function and assert the expected behavior
                    result = query_data("test2-instance", "test7-database", "USA")

                    assert mock_spanner_client.instance.call_count == 1
                    assert mock_instance.database.call_count == 1
                    assert mock_database.snapshot.call_count == 1
                    assert mock_snapshot.execute_sql.call_count == 1

                    assert result == mock_results

    
   @app.get("/attributes")
def get_attribute_by_country(country:str):
    res = AudienceAttributeService().get_attribute_by_country(country)
    if not res:
        raise HTTPException(status_code=400,detail="No country is present")
    return res 
