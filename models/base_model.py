#!/usr/bin/python3

import json
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:

    id: str
    created_at: datetime
    updated_at: datetime

    UNCHANGEABLE_ATTRS = ["id", "created_at", "updated_at"]

    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            for kw in kwargs:
                if kw == "created_at" and isinstance(kwargs[kw], str):
                    setattr(
                        self, kw, datetime.strptime(kwargs[kw], "%Y-%m-%dT%H:%M:%S.%f")
                    )
                elif kw == "updated_at" and isinstance(kwargs[kw], str):
                    setattr(
                        self, kw, datetime.strptime(kwargs[kw], "%Y-%m-%dT%H:%M:%S.%f")
                    )
                elif kw != "__class__":
                    setattr(self, kw, kwargs[kw])

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        models.storage.new(self)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self) -> dict:
        _dict = {**self.__dict__}

        if "created_at" in _dict.keys():
            _dict["created_at"] = self.created_at.isoformat()

        if "updated_at" in _dict.keys():
            _dict["updated_at"] = self.updated_at.isoformat()

        _dict["__class__"] = self.__class__.__name__

        return _dict

    def __str__(self) -> str:
        return "[{class_name}] ({id}) {_dict}".format(
            class_name=self.__class__.__name__,
            id=self.id,
            # TODO: remove json parse
            # _dict=self.__dict__
            _dict=json.dumps(self.to_dict(), indent=2),
        )

    @classmethod
    def all(cls):
        _all = models.storage.all()
        items = []

        for k in _all:
            if isinstance(_all[k], cls):
                items.append(_all[k])

        return items
