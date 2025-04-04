import struct
from typing import Any, Dict, Union


class ProtoDef:
    def __init__(self, schema: Dict[str, Any]):
        """
        Initialize ProtoDef with a schema definition.
        """
        self.schema = schema

    def serialize(self, data: Dict[str, Any]) -> bytes:
        """
        Serialize a dictionary based on the schema.
        """
        buffer = b""
        for field in self.schema["fields"]:
            name, dtype = field["name"], field["type"]
            value = data[name]
            buffer += self._encode(dtype, value)
        return buffer

    def deserialize(self, binary: bytes) -> Dict[str, Any]:
        """
        Deserialize binary data into a dictionary based on the schema.
        """
        data = {}
        offset = 0
        for field in self.schema["fields"]:
            name, dtype = field["name"], field["type"]
            value, size = self._decode(dtype, binary[offset:])
            data[name] = value
            offset += size
        return data

    def _encode(self, dtype: str, value: Any) -> bytes:
        """
        Encode values based on the given data type.
        """
        if dtype == "int":
            return struct.pack("!i", value)  # fix to 4-byte integer
        elif dtype == "float":
            return struct.pack("!f", value)  # fix to 4-byte float
        elif dtype == "string":
            encoded = value.encode("utf-8")
            return struct.pack("!I", len(encoded)) + encoded
        else:
            raise ValueError(f"Unsupported type: {dtype}")

    def _decode(self, dtype: str, binary: bytes) -> Union[Any, int]:
        """
        Decode binary data based on the given data type.
        """
        if dtype == "int":
            return struct.unpack("!i", binary[:4])[0], 4
        elif dtype == "float":
            return struct.unpack("!f", binary[:4])[0], 4
        elif dtype == "string":
            length = struct.unpack("!I", binary[:4])[0]
            return binary[4:4+length].decode("utf-8"), 4 + length
        else:
            raise ValueError(f"Unsupported type: {dtype}")

