#!/usr/bin/python3
# This is the entry point of the command interpreter

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

dic_class = {'BaseModel': BaseModel, 'User': User, 'State': State, 'City': City, 'Amenity': Amenity, 'Place': Place, 'Review': Review}

list_class = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]


class HBNBCommand(cmd.Cmd):
    "Command interpreter"
    prompt = "(hbnb)"

    def do_EOF(self, args):
        "EOF command to exit the program\n"
        return(True)

    def do_quit(self, args):
        "Quit command to exit the program\n"
        return(True)

    def emptyline(self):
        "If there is an empty line, it just pass"
        pass

    def do_create(self, args):
        "creates an instance of Base"
        list_arg = args.split()
        if len(list_arg) == 0:
            print("** class name missing **")
        if list_arg[0] in dic_class:
            instance = dic_class[list_arg[0]]()
            print(instance.id)
            instance.save()
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        " Deletes an instance based on the class name and id "
        args_ls = args.split()

        if len(args_ls) == 0:
            print("** class name missing **")
        elif len(args_ls) == 1 and args_ls[0] not in list_class:
            print("** class doesn't exist **")
        elif len(args_ls) == 1:
            print("** instance id missing **")
        elif len(args_ls) == 2:
            key = args_ls[0] + '.' + args_ls[1]
            if key in models.storage.all():
                models.storage.all().pop(key)
                models.storage.save()
            else:
                print("** no instance found **")
        

    def do_all(self, args):
        " Prints all string representation of all instances "
        args_ls = args.split()
        dic_all = storage.all()

        if len(args_ls) == 0:
            for key in dic_all.keys():
                print(dic_all[key])
        else:
            if len(args_ls) == 1 and args_ls[0] not in list_class:
                print("** class doesn't exist **")
            else:
                for id_key in dic_all.keys():
                    if (dic_all[id_key] == args_ls[0]):
                        print(dic_all[id_key])


if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.cmdloop()
