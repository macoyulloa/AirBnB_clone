#!/usr/bin/python3

import os
import json
from pathlib import Path

class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        " return the all dictionary "
        return self.__objects

    def new(self, obj):
        " sets the object with the key "
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        " serializes objects to the JSON file "
        filename = FileStorage.__file_path
        with open(filename, "w") as my_file:
            objc = my_file.read()
            for key, value in objc: 
                json.dumps(my_file)

    def reload(self):
        " deserializes the JSON file to objects "
        filename = FileStorage.__file_path
        file_exist = Path(filename)
        if file_exist.exists():
            with open(filename, "r") as my_file:
                objc = my_file.read()
                new_dic = json.loads(objc)
                for key, value in new_dic:
                    FileStorage.__objects[key] = value["__class__"](**value)
        else:
            pass

