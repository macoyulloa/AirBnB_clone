#!/usr/bin/env python3
# This is the entry point of the command interpreter

import cmd

class HBNBCommand(cmd.Cmd):
    "Command interpreter"
    prompt = "(hbnb) "

    def do_EOF(self, args):
        "interpreter exit"
        return(True)

    def do_quit(self, args):
        "interpreter exit" 
        return(True)

    def emptyline(self):
        "If the user does not digit any command" 
        pass

    def precmd(self, args):
        "Before execute a method, convert the cmd in lower-case"
        args = args.lower()
        return(args)



if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.cmdloop()
