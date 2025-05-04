
# Postman2OpenAPI

A Python module to convert Postman collections to OpenAPI (Swagger) format without any third-party dependencies.

## Installation

```bash
pip install postman2openapi
```

## Usage

```python
from postman2openapi import PostmanToOpenAPIConverter, read_postman_collection, write_openapi_spec

# Read your Postman collection
collection_data = read_postman_collection("path/to/collection.json")

# Create converter instance
converter = PostmanToOpenAPIConverter()

# Convert to OpenAPI
openapi_spec = converter.parse_postman_collection(collection_data)

# Save as YAML (default) or JSON
write_openapi_spec(openapi_spec, "openapi_spec.yaml")  # For YAML
write_openapi_spec(openapi_spec, "openapi_spec.json", format="json")  # For JSON
```

## Features

- Converts Postman collections to OpenAPI 3.0.0 specification
- Supports:
  - Basic request information (URL, method, description)
  - Query parameters
  - Request bodies (JSON and form-data)
  - Path parameters
  - Folder structure
- No third-party dependencies except PyYAML
- Outputs in both YAML and JSON formats

## Development

To set up the development environment:

```bash
# Clone the repository
git clone https://github.com/Pulkit-Py/postman2openapi.git
cd postman2openapi

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Author

Created by [Pulkit-Py](https://github.com/Pulkit-Py)

### Connect with Me

- 🌐 Website: [Py Digital Solution](https://www.pydigitalsolution.me/)
- 💼 LinkedIn: [Pulkit-Py](https://www.linkedin.com/in/pulkit-py/)
- 📸 Instagram: [@pulkit.py](https://www.instagram.com/pulkit_py/)
- 🐙 GitHub: [@Pulkit-Py](https://github.com/Pulkit-Py)

## Package Information

- **Version**: 1.0.0
- **Last Updated**: 2025-05-04
- **Created**: 2025-05-04
- **PyPI**: [postman2openapi](https://pypi.org/project/postman2openapi/)

## Support

If you found this project helpful, consider:
- Giving it a ⭐ on GitHub
- Following me on social media
- Sharing it with others who might find it useful

---
<p align="center">Made with ❤️ by <a href="https://github.com/Pulkit-Py">Pulkit-Py</a> From 🇮🇳 India</p>