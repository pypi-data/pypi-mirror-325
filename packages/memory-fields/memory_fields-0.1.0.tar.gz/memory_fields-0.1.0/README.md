# Memory Fields

**Memory Fields** is a Python client for interacting with the **SenTech AI Memory API**, enabling users to add, query, and manage memory fields efficiently.

## Installation

You can install the package using `pip`:

```bash
pip install memory-fields
```

## Usage

### Import and Initialize the Client**
```python
from memory_fields import EMFClient

# Replace 'your_api_key' with a valid API key
client = EMFClient(api_key="your_api_key")
```

### Add Memory to a Field**

```python
response = client.add_memory(
    field_id="12345",
    content="This is a test memory.",
    timestamp=1700000000
)
print(response)
```

### Query Memories**
```python
results = client.query_memory(field_id="12345", query="What do I remember?")
print(results)
```

### Query with an Image**
```python
image_results = client.query_image(field_id="12345", image_path="sample.jpg")
print(image_results)
```

## API Methods

| Method | Description |
|--------|-------------|
| `add_memory(field_id, content, timestamp, relevance=1.0, decay_rate=0.01, salience=1.0)` | Adds a memory to a specified field. |
| `query_memory(field_id, query, top_k=50, depth_k=3)` | Searches a field for relevant memories based on a text query. |
| `query_image(field_id, query=None, image_path=None, top_k=50)` | Performs a combined query using text and an optional image. |

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Contact

For support or inquiries, reach out via [GitHub Issues](https://github.com/yourusername/memory-fields/issues).
or 
email us at service@sentech.ai