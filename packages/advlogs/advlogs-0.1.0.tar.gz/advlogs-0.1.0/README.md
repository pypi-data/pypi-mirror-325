# advlogs

`advlogs` is an advanced logging library that enhances traditional logging with **AES encryption, Gzip compression, and multi-threading**.

## Features

- **AES encryption for secure logs**
- **Gzip compression for storage efficiency**
- **Multi-threaded logging**
- **Structured JSON logging**

## Installation

```bash
pip install advlogs


USAGE:
from advlogs import advlogs
from cryptography.fernet import Fernet

key = Fernet.generate_key().decode()
logger = advlogs(log_file="advlogs.log", encrypt=True, key=key)

logger.log("INFO", "This is an encrypted log message.")
logger.compress_logs()
```
