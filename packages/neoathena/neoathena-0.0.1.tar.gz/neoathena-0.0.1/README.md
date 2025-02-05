# NeoAthena Python Client

A Python client library for interacting with the NeoAthena API, providing functionality to create and manage collections, upload files, and perform document retrieval operations.

## Installation

```bash
pip install neoathena
```

## Quick Start

```python
from neoathena import NeoAthenaClient

# Initialize the client
client = NeoAthenaClient(api_key="your-api-key")

# Check if the collection exists, create it if it doesn't, and upload the file to the collection
results =client.upload_to_collection(collection_name="your-collection-name",filepath="path/to/your/file")

# Retrieve documents based on a query
results = client.retrieve_from_collection(collection_name="your-collection-name", query="your search query", top_k=4)

# List your collections
result=client.get_collections()

```

## Features

- Create collection and upload files with automatic content type detection
- Perform semantic search queries
- Delete individual documents or entire collections
- List all user collections
- Built-in error handling and validation

## API Reference

### Create a Collection and Upload Files

```python
client = NeoAthenaClient(api_key="your-api-key")
results =client.upload_to_collection(
    collection_name="your-collection-name",
    filepath="path/to/your/file"
    )
```

### Retrieving Documents

```python
results = client.retrieve_from_collection
(
    collection_name="your-collection-name", 
    query="your search query", 
    top_k=4
)
```

### Deleting Documents

Delete a specific document:
```python
response = client.delete_from_collection(
    collection_name="your-collection-name",
    doc_id=123
)
```

Delete all documents:
```python
response = client.delete_from_collection(
    collection_name="your-collection-name",
    doc_id=0,
    delete_all=True
)
```

### Deleting a Collection

```python
response = client.delete_collection(collection_name="your-collection-name")
```

### List user collection

```python
response = client.get_collections()
```

## Error Handling

The client includes comprehensive error handling for common scenarios:

- `ValueError`: Raised for invalid input parameters
- `FileNotFoundError`: Raised when specified files don't exist
- `requests.exceptions.RequestException`: Raised for network-related errors

Example error handling:

```python
try:
    response = client.upload_to_collection(api_key, "file.pdf")
except FileNotFoundError:
    print("File not found")
except ValueError as e:
    print(f"Invalid input: {e}")
except requests.exceptions.RequestException as e:
    print(f"API request failed: {e}")
```

## Requirements

- Python 3.7+
- requests library
- Valid API credentials

## License

MIT License

## Support

For support, please contact support@raen.ai or visit [sso.raen.ai](https://sso.raen.ai)