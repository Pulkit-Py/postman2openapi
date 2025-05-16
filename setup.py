from setuptools import setup, find_packages
from datetime import datetime

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="postman2openapi",
    version="1.0.1",  # Updated version
    author="Pulkit-Py",
    author_email="your.email@example.com",
    description="Convert Postman Collections to OpenAPI (Swagger) specification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pulkit-Py/postman2openapi",
    project_urls={
        "Bug Tracker": "https://github.com/Pulkit-Py/postman2openapi/issues",
        "Documentation": "https://github.com/Pulkit-Py/postman2openapi#readme",
        "Source Code": "https://github.com/Pulkit-Py/postman2openapi",
    },
    keywords=[
        "postman",
        "openapi",
        "swagger",
        "api",
        "converter",
        "documentation",
        "rest",
        "api-documentation",
        "postman-collection",
        "openapi-specification"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Documentation",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[
        "pyyaml>=5.1",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=22.0",
            "isort>=5.0",
            "flake8>=3.9",
        ],
    },
)