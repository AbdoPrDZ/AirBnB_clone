#!/usr/bin/python3

import json

import models
from models.base_model import BaseModel


class FileStorage:

    __file_path: str = "file.json"
    __objects: dict[str, BaseModel] = {}

    def all(self) -> dict[str, BaseModel]:
        return FileStorage.__objects

    def new(self, obj):
        k = "{obj_name}.{id}".format(obj_name=obj.__class__.__name__, id=obj.id)

        FileStorage.__objects[k] = obj

    def save(self):
        _dicts = {}

        for key in FileStorage.__objects:
            _dicts[key] = FileStorage.__objects[key].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            # TODO:remove indent
            json.dump(_dicts, f, indent=2)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                _json = json.load(f)

                for k in _json:
                    obj = _json[k]
                    _class = models.CLASSES[obj["__class__"]]

                    self.new(_class(**obj))
        except FileNotFoundError:
            pass
