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
import shlex

dic_class = {'BaseModel': BaseModel,
             'User': User, 'State': State,
             'City': City, 'Amenity': Amenity,
             'Place': Place, 'Review': Review}

list_class = ["BaseModel", "User", "State",
              "City", "Amenity", "Place", "Review"]

dic_all = models.storage.all()


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

    def do_show(self, args):
        "print representation based of id"
        list_arg = args.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] is None:
            print("** class doesn't exist **")
        elif len(list_arg) == 1:
            print("** instance id missing **")
        elif list_arg[0] not in dic_class:
            print("** class doesn't exist **")
        else:
            instance = models.storage.all()
            for key, value in instance.items():
                if key == list_arg[0] + '.' + list_arg[1]:
                    print(value)
                    return
            print("** no instance found **")

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
        dic_all = models.storage.all()
        ls_values = []

        if len(args_ls) == 0:
            for value in dic_all.values():
                ls_values.append(str(value))
                print(ls_values)
        else:
            if len(args_ls) == 1 and args_ls[0] not in list_class:
                print("** class doesn't exist **")
            else:
                for key, values in dic_all.items():
                    token = key.split('.')
                    if (token[0] == args_ls[0]):
                        ls_values.append(str(values))
                print(ls_values)

    def do_update(self, args):
        'update the instance'
        list_arg = shlex.split(args)
        if len(list_arg) == 0:
            print("** class name missing **")
        elif len(list_arg) == 1 and list_arg[0] not in list_class:
            print("** class doesn't exist **")
        elif len(list_arg) == 1:
            print("** instance id missing **")
        elif len(list_arg) == 2:
            print("** attribute name missing **")
        elif len(list_arg) == 3:
            print("** value missing **")
        else:
            key = ''
            key = list_arg[0] + '.' + list_arg[1]
            if key in dic_all:
                setattr(dic_all[key], list_arg[2], list_arg[3])
                models.storage.save()
            else:
                print("** no instance found **")
                return

if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.cmdloop()
