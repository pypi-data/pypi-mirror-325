# Cloud DB Connector

A unified cloud storage package that provides seamless integration with major cloud providers: Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platform (GCP). This library allows developers to easily access and manage cloud storage services with a consistent interface.

## Package Structure

```plaintext
- database_manager.py      # Factory function to create DB connection based on the service type
- db_connection.py         # Interface to get DB connection
- rds_execute.py           # RDS SQL operations
```

## Features

- **Supports Multiple Cloud Providers**: Easily switch between AWS, Azure, and GCP.
- **Flexible Configuration**: Configure services with required parameters for each provider.
- **Intuitive API**: Simple methods for managing cloud storage operations.

## Installation
Ensure all necessary dependencies are installed:
```python
pip install cloud_db_connector
```

## Usage
```python
#! pip install cloud_db_connector

from cloud_db_connector import get_cloud_db_service
aws_service = get_cloud_db_service(
    service='aws',
    hostname='abc-dev-sandbox.cluster-cgjdfh3jkv0.us.rds.amazonaws.com',
    port=3306,
    username='Username',
    password="Password",
    database='ConnexaDev',
    region='us-east-1'
    )

query = "SELECT * FROM person LIMIT 1;"
results = aws_service.execute(query)

print("Query Results:")
for row in results:
    print(row)
```
