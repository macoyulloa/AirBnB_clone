#!/usr/bin/python3
"""
this is parent class that inherates to the other class
"""


import uuid
from datetime import datetime
from models. import storage
import json


time = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    'define the base model class'

    def __init__(self, *args, **kwargs):
        'init with args and kwgards'  
        if kwargs:
            self.__dict__ = kwargs
            if "created_at" in kwargs:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            if "updated_at" in kwargs:
                self.update_at = datetime.strptime(kwargs["updated_at"], time)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.update_at = datetime.now()
            storage.new(self)
            storage.save()
            
    def save(self):
        'public method for update datetime'
        self.updated_at = datetime.now()
        storage.save()

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
