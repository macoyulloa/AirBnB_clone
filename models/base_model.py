#!/usr/bin/python3
"""
this is the base class for the prompt
"""


import uuid
from datetime import datetime
import json

class BaseModel:
    'define the base model class'

    def __init__(self, *args, **kwargs):
        'init with args and kwards'
        if kwargs:
            #necesario completar
    
    def save(self):
        'public method for datetime'
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        'dictionary format'
        dct = self.__dict__.copy()
        dct['__class__'] = self.__class__.__name__
        dct['created_at'] = self.created_at.isoformat()
        dct['updated_at'] = self.updated_at.isoformat()
        return dct
        
    def __str__(self):
        'define magic method to format'
        return ("[{}] ({}) {}".format(self.__class__.__name__, str(self.id),
                                     self.__dict__))
