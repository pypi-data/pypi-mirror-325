# advjson

`advjson` provides secure and optimized JSON handling with **AES encryption, Gzip compression, schema validation, and multi-threading**.

## Features

- **Gzip compression for efficient storage**
- **AES encryption for secure JSON storage**
- **JSON schema validation**
- **Multi-threaded JSON compression**
- **Automatic key generation**

## Installation

```bash
pip install advjson


USAGE:
from advjson import advjson

data = {"username": "Brewlock", "role": "admin"}
key = advjson.generate_key()

compressed = advjson.compress_json(data)
decompressed = advjson.decompress_json(compressed)

encrypted = advjson.encrypt_json(data, key)
decrypted = advjson.decrypt_json(encrypted, key)

schema = {"type": "object", "properties": {"username": {"type": "string"}, "role": {"type": "string"}}}
is_valid = advjson.validate_json(data, schema)
```
