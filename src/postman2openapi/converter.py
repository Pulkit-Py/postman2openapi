
import json
import yaml
from typing import Dict, Any, List
from datetime import datetime

class PostmanToOpenAPIConverter:
    def __init__(self):
        self.openapi_version = "3.0.0"
        self.converted_paths = {}
        self.schemas = {}
        
    def parse_postman_collection(self, collection_data: Dict[str, Any]) -> Dict[str, Any]:
        """Parse a Postman collection and convert it to OpenAPI format."""
        openapi_spec = {
            "openapi": self.openapi_version,
            "info": self._generate_info(collection_data),
            "paths": {},
            "components": {
                "schemas": {},
                "securitySchemes": {}
            }
        }
        
        # Process items in the collection
        if "item" in collection_data:
            self._process_items(collection_data["item"])
            openapi_spec["paths"] = self.converted_paths
            
        return openapi_spec
    
    def _generate_info(self, collection_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate the OpenAPI info section from Postman collection data."""
        info = {
            "title": collection_data.get("info", {}).get("name", "Converted API"),
            "description": collection_data.get("info", {}).get("description", ""),
            "version": collection_data.get("info", {}).get("version", "1.0.0")
        }
        return info
    
    def _process_items(self, items: List[Dict[str, Any]], parent_path: str = "") -> None:
        """Process Postman collection items recursively."""
        for item in items:
            if "item" in item:  # This is a folder
                folder_path = f"{parent_path}/{item['name']}" if parent_path else item['name']
                self._process_items(item["item"], folder_path)
            else:  # This is a request
                self._process_request(item, parent_path)
    
    def _process_request(self, request_item: Dict[str, Any], parent_path: str) -> None:
        """Process a single request item and convert it to OpenAPI path format."""
        if "request" not in request_item:
            return
            
        request = request_item["request"]
        method = request.get("method", "GET").lower()
        
        # Extract URL and path parameters
        url_data = request.get("url", {})
        path = self._process_url(url_data, parent_path)
        
        # Create path item
        if path not in self.converted_paths:
            self.converted_paths[path] = {}
            
        # Create operation object
        operation = {
            "summary": request_item.get("name", ""),
            "description": request.get("description", ""),
            "responses": self._generate_default_response(),
        }
        
        # Process query parameters
        query_params = self._process_query_params(url_data)
        if query_params:
            operation["parameters"] = query_params
            
        # Process request body
        if "body" in request:
            operation["requestBody"] = self._process_request_body(request["body"])
            
        self.converted_paths[path][method] = operation
    
    def _process_url(self, url_data: Dict[str, Any], parent_path: str) -> str:
        """Process URL data and return OpenAPI path."""
        if isinstance(url_data, str):
            return url_data
            
        path_segments = []
        if parent_path:
            path_segments.append(parent_path)
            
        if "path" in url_data:
            for segment in url_data["path"]:
                if isinstance(segment, dict) and "value" in segment:
                    path_segments.append(f"{{{segment['value']}}}")
                else:
                    path_segments.append(str(segment))
                    
        return "/" + "/".join(filter(None, path_segments))
    
    def _process_query_params(self, url_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Process query parameters from URL data."""
        parameters = []
        if "query" in url_data:
            for query in url_data["query"]:
                param = {
                    "name": query.get("key", ""),
                    "in": "query",
                    "description": query.get("description", ""),
                    "required": query.get("required", False),
                    "schema": {
                        "type": "string"
                    }
                }
                parameters.append(param)
        return parameters
    
    def _process_request_body(self, body_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process request body data."""
        request_body = {
            "required": True,
            "content": {}
        }
        
        mode = body_data.get("mode", "raw")
        if mode == "raw":
            content_type = "application/json"
            try:
                # Try to parse as JSON to generate schema
                json_data = json.loads(body_data.get("raw", "{}"))
                schema = self._generate_schema(json_data)
                request_body["content"][content_type] = {
                    "schema": schema
                }
            except json.JSONDecodeError:
                # Fallback for non-JSON raw body
                request_body["content"]["text/plain"] = {
                    "schema": {
                        "type": "string"
                    }
                }
        elif mode == "formdata":
            request_body["content"]["multipart/form-data"] = {
                "schema": self._process_form_data(body_data.get("formdata", []))
            }
            
        return request_body
    
    def _generate_schema(self, data: Any) -> Dict[str, Any]:
        """Generate JSON Schema from sample data."""
        if isinstance(data, dict):
            properties = {}
            for key, value in data.items():
                properties[key] = self._generate_schema(value)
            return {
                "type": "object",
                "properties": properties
            }
        elif isinstance(data, list):
            if data:
                return {
                    "type": "array",
                    "items": self._generate_schema(data[0])
                }
            return {
                "type": "array",
                "items": {}
            }
        elif isinstance(data, bool):
            return {"type": "boolean"}
        elif isinstance(data, int):
            return {"type": "integer"}
        elif isinstance(data, float):
            return {"type": "number"}
        elif isinstance(data, str):
            return {"type": "string"}
        elif data is None:
            return {"type": "null"}
        return {}
    
    def _process_form_data(self, formdata: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Process form data parameters."""
        properties = {}
        for item in formdata:
            properties[item.get("key", "")] = {
                "type": "string",
                "description": item.get("description", "")
            }
        return {
            "type": "object",
            "properties": properties
        }
    
    def _generate_default_response(self) -> Dict[str, Any]:
        """Generate a default response object."""
        return {
            "200": {
                "description": "Successful response",
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object"
                        }
                    }
                }
            }
        }