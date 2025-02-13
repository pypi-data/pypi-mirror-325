# advhashlib

`advhashlib` is an advanced cryptographic hashing library, improving security, speed, and multi-threaded hashing capabilities.

## Features

- **Salted SHA-256 & SHA-512 hashing**
- **HMAC-based authentication signatures**
- **Multi-threaded hashing for large datasets**
- **Cryptographic-grade security**

## Installation

```bash
pip install advhashlib
```

from advhashlib import advhashlib

print(advhashlib.sha256("secure_data")) # Salted SHA-256
print(advhashlib.hmac_sha256("secret_key", "message")) # HMAC Authentication
hashes = advhashlib.multi_threaded_hash(["data1", "data2"]) # Multi-threaded hashing
