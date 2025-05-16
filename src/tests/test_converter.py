import pytest
from postman2openapi import PostmanToOpenAPIConverter

def test_converter_initialization():
    converter = PostmanToOpenAPIConverter()
    assert converter.openapi_version == "3.0.0"
    assert converter.converted_paths == {}
    assert converter.schemas == {}

def test_basic_collection_conversion():
    converter = PostmanToOpenAPIConverter()
    
    # Sample Postman collection
    collection_data = {
        "info": {
            "name": "Test API",
            "description": "Test Description",
            "version": "1.0.0"
        },
        "item": [
            {
                "name": "Test Request",
                "request": {
                    "method": "GET",
                    "url": {
                        "raw": "https://api.example.com/test",
                        "path": ["test"]
                    }
                }
            }
        ]
    }
    
    result = converter.parse_postman_collection(collection_data)
    
    assert result["info"]["title"] == "Test API"
    assert result["info"]["version"] == "1.0.0"
    assert "/test" in result["paths"]
    assert "get" in result["paths"]["/test"]