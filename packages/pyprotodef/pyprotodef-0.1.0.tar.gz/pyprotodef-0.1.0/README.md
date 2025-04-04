# PyProtoDef

PyProtoDef is a Python package for defining and handling binary protocols, inspired by ProtoDef.

## Features
✅ Compact binary serialization  
✅ Faster parsing than JSON  
✅ Strong data typing (int, float, string)  
✅ Ideal for networking, gaming, and IoT  

## Installation

```sh
pip install pyprotodef

## Usage Example

To try out PyProtoDef, create a new file (for example, example.py) with the following content:

```python
from pyprotodef import ProtoDef

# Define a schema
schema = {
    "name": "player_data",
    "fields": [
        {"name": "id", "type": "int"},
        {"name": "score", "type": "float"},
        {"name": "nickname", "type": "string"}
    ]
}

# Create a ProtoDef instance
proto = ProtoDef(schema)

# Serialize data
data = {"id": 123, "score": 99.5, "nickname": "PlayerOne"}
binary_data = proto.serialize(data)

# Deserialize data
parsed_data = proto.deserialize(binary_data)

print("Serialized:", binary_data)
print("Deserialized:", parsed_data)
```

Then, run the example with:

```sh
python example.py
```
