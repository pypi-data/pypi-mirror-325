# advsecrets

`advsecrets` is an advanced cryptographic security library for secure token and key generation.

## Features

- **High-entropy secure tokens**
- **Secure UUID generation**
- **Multi-threaded token generation**
- **Strong password generator**

## Installation

```bash
pip install advsecrets
```

from advsecrets import advsecrets

print(advsecrets.secure_token()) # Secure 32-byte token
print(advsecrets.secure_uuid()) # Secure UUID
print(advsecrets.multi_threaded_tokens(5)) # Generate 5 tokens in parallel
print(advsecrets.secure_password(16)) # Generate a secure password
