import json
import yaml
from pathlib import Path
from typing import Dict, Any

def read_postman_collection(file_path: str) -> Dict[str, Any]:
    """Read a Postman collection from a JSON file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_openapi_spec(spec: Dict[str, Any], output_path: str, format: str = 'yaml') -> None:
    """Write the OpenAPI specification to a file."""
    output_path = Path(output_path)
    
    if format.lower() == 'json':
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(spec, f, indent=2)
    else:
        with open(output_path, 'w', encoding='utf-8') as f:
            yaml.dump(spec, f, sort_keys=False, allow_unicode=True)