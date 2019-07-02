#!/usr/bin/env python3
# This is the entry point of the command interpreter

import cmd


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

    def create(self, args):
        "creates an instance of Base"
        args = args.split()
        if len(args) < 1:
            print("** class name missing **")
        if args[0] is None:
            print("** class doesn't exist **")
        else:
            
            
          

    def destroy(self, args):
        'destroy an instance'
        

if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.cmdloop()
