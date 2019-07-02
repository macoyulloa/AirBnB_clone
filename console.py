#!/usr/bin/env python3
# This is the entry point of the command interpreter

import cmd
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class HBNBCommand(cmd.Cmd):
    "Command interpreter"
    prompt = "(hbnb) "

    def do_EOF(self, args):
        "EOF command to exit the program\n"
        return(True)

    def do_quit(self, args):
        "Quit command to exit the program\n"
        return(True)

    def emptyline(self):
        "If there is an empty line, it just pass"
        pass

    def precmd(self, args):
        "Before execute a method, convert the cmds in lower-case"
        args = args.lower()
        return(args)


if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.cmdloop()
