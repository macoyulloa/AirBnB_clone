#!/usr/bin/python3
"""
this is parent class that inherates to the other class
"""


from uuid import uuid4
from datetime import datetime
import models
import json


time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():
    'define the base model class'
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at":
                    self.created_at = datetime.strptime
                    (kwargs["created_at"], time)
                if key == "updated_at":
                    self.updated_at = datetime.strptime
                    (kwargs["updated_at"], time)
                self.__setattr__(key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def save(self):
        'public method for update datetime'
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        'dictionary format'
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return(new_dict)

    def __str__(self):
        'define magic method to format'
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                      self.__dict__))
