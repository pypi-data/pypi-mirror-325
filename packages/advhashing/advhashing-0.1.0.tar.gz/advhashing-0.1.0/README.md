# advhashing

`advhashing` is an advanced cryptographic hashing library with enhanced security features.

## Features

- **Salted SHA-256 & SHA-512 hashing**
- **HMAC-based authentication**
- **Multi-threaded hashing for large datasets**
- **High-speed and cryptographic-grade security**

## Installation

```bash
pip install advhashing

USAGE:
from advhashing import advhashing

print(advhashing.hash_sha256("secure_data"))  # Salted SHA-256
print(advhashing.hmac_sha256("secret_key", "message"))  # HMAC Authentication
hashes = advhashing.multi_threaded_hash(["data1", "data2"])  # Multi-threaded hashing
```
