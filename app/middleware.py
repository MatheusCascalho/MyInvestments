import yaml
import json
from typing import Dict, Any
from tinydb.storages import Storage
from dataclasses import asdict, is_dataclass
from enum import Enum
from flask import jsonify


class Encoder(json.JSONEncoder):
    OBJ_CLASS = Any

    def default(self, o: Any) -> Any:
        transformations = {
            "Enum": lambda x: x.name.lower(),
            "datetime": str,
            "date": str,
            "dataclass": asdict,
            "dict": self.decode_dictionaries,
        }
        if is_dataclass(o):
            class_name = "dataclass"
        elif isinstance(o, Enum):
            class_name = "Enum"
        else:
            class_name = o.__class__.__name__
        if class_name in transformations:
            return transformations[class_name](o)
        return o
        # return str(o)

    def decode_dictionaries(self, dictionary):
        original_keys = list(dictionary.keys())
        new_dictionary = {}
        for key in dictionary:
            new_dictionary[str(key)] = self.default(dictionary[key])

        return new_dictionary



class YAMLStorage(Storage):
    def __init__(self, filename, **kwargs):
        self.filename = filename

    def write(self, data: Dict[str, Dict[str, Any]]) -> None:
        with open(self.filename,'w+') as handle:
            json.dump(data, handle, cls=Encoder, indent=2, ensure_ascii=False)

    def read(self):
        with open(self.filename) as handle:
            try:
                data = yaml.safe_load(handle.read())  # (2)
                return data
            except yaml.YAMLError:
                return None  # (3)

    def close(self):  # (4)
        pass