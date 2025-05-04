import pytest
import json
import yaml
from pathlib import Path
from postman2openapi.utils import read_postman_collection, write_openapi_spec

def test_read_postman_collection(tmp_path):
    # Create a temporary Postman collection file
    collection_data = {
        "info": {"name": "Test Collection"},
        "item": []
    }
    collection_file = tmp_path / "collection.json"
    collection_file.write_text(json.dumps(collection_data))
    
    # Test reading the collection
    result = read_postman_collection(str(collection_file))
    assert result["info"]["name"] == "Test Collection"

def test_write_openapi_spec_yaml(tmp_path):
    spec_data = {"openapi": "3.0.0"}
    output_file = tmp_path / "spec.yaml"
    
    write_openapi_spec(spec_data, str(output_file))
    
    # Verify the written file
    assert output_file.exists()
    with open(output_file) as f:
        loaded_data = yaml.safe_load(f)
    assert loaded_data["openapi"] == "3.0.0"

def test_write_openapi_spec_json(tmp_path):
    spec_data = {"openapi": "3.0.0"}
    output_file = tmp_path / "spec.json"
    
    write_openapi_spec(spec_data, str(output_file), format="json")
    
    # Verify the written file
    assert output_file.exists()
    with open(output_file) as f:
        loaded_data = json.load(f)
    assert loaded_data["openapi"] == "3.0.0"