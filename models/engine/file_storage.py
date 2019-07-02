#!/usr/bin/python3

import os
import json
from pathlib import Path
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        " return the all dictionary "
        return FileStorage.__objects

    def new(self, obj):
        " sets the object with the key "
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        " serializes objects to the JSON file "
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        filename = FileStorage.__file_path
        with open(filename, "w") as my_file:
            my_file.write(json.dumps(new_dict))

    def reload(self):
        " deserializes the JSON file to objects "
        filename = FileStorage.__file_path
        file_exist = Path(filename)
        if file_exist.exists():
            with open(filename, "r") as my_file:
                new_dic = json.load(my_file)
                for key, value in new_dic.items():
                    FileStorage.__objects[key] = eval(value["__class__"])(value)
        else:
            pass
