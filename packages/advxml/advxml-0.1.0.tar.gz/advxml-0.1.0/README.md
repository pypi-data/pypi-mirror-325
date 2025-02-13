# advxml

`advxml` is an advanced XML processing library that enhances traditional XML handling with **AES encryption, Gzip compression, and schema validation**.

## Features

- **Gzip compression for efficient XML storage**
- **AES encryption for secure XML storage**
- **XML Schema (XSD) validation**
- **Multi-threaded XML compression**
- **Automatic key generation**

## Installation

```bash
pip install advxml

USAGE:
from advxml import advxml

data = {"username": "Brewlock", "role": "admin"}
xml_str = advxml.to_xml(data)

compressed = advxml.compress_xml(xml_str)
decompressed = advxml.decompress_xml(compressed)

key = advxml.generate_key()
encrypted = advxml.encrypt_xml(xml_str, key)
decrypted = advxml.decrypt_xml(encrypted, key)
```
