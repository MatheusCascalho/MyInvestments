import yaml
import json
from typing import Dict, Any
from tinydb.storages import Storage
from dataclasses import asdict, is_dataclass
from enum import Enum


class Encoder(json.JSONEncoder):
    OBJ_CLASS = Any
    def default(self, o: Any) -> Any:
        transformations = {
            "Enum": lambda x: x.name.lower(),
            "datetime": str,
            "date": str,
            "dataclass": asdict
        }
        if is_dataclass(o):
            class_name = "dataclass"
        elif isinstance(o, Enum):
            class_name = "Enum"
        else:
            class_name = o.__class__.__name__
        if class_name in transformations:
            return transformations[class_name](o)
        else:
            return json.JSONEncoder.default(self, o)


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