# AirBnB_clone 
### Welcome to the AirBnB clone project! (The Holberton B&B 
### First step: Write a command interpreter to manage your AirBnB objects.

![](AirBnB.PNG)

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

## What’s a command interpreter?

A command interprepart of a computer operating system that understands and executes commands that are entered interactively by a human being or from a program. In some operating systems, the command interpreter is called the shell.

This command interpreter could manage the objects of the all projects:

```
Create a new object (: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object
```

## Getting Started
In order to dowload the program and runs the command interpreter, it is necesary to copy the repository in your computer using the:
```
git clone <url>
```
To execute the program it is important to run the console file using the ./console.py, it is going to:
```
./console.py
```
That is all, let´s get into the command line interpreter!!

## FILES AND DIRECTORIES 

```
1. models directory contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
2. tests directory will contain all unit tests.
3. console.py file is the entry point of our command interpreter.
4. models/base_model.py file is the base class of all our models. It contains common elements:
   - attributes: id, created_at and updated_at
   - methods: save() and to_json()
5. models/engine directory will contain all storage classes (using the same prototype). For the moment you will have only one: file_storage.py.

```

## In order to understand & Running the program

### SYNOPSIS

The console is a command interprepart of a computer operating system that understands and executes commands that are entered interactively by a human being or from a program.

### DESCRIPTION

The first piece is to mante a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine.

### CONSOLE

The console console.py contains the entry point od the command interpreter:

```
~/AirBnB$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb) help quit
Quit command to exit the program

(hbnb)
(hbnb)
(hbnb) quit 
:~/AirBnB$

```

### COMMANDS

1. create: Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
```
Ex: $ create BaseModel
```

2. show: Prints the string representation of an instance based on the class name and id. 
```
Ex: $ show BaseModel 1234-1234-1234
```

3. destroy: Deletes an instance based on the class name and id (save the change into the JSON file)
``` 
Ex: $ destroy BaseModel 1234-1234-1234
```

4. all: Prints all string representation of all instances based or not on the class name
``` 
Ex: $ all BaseModel or $ all
```

5. update: Updates an instance based on the class name and id by adding or updating attribute (save thge into the JSON file).
```
Ex: $ update BaseMo-1234-1234 email "aibnb@holbertonschool.com"
```

#### EXAMPLES

##### cd command

The 'cd' commnad let us change the current directory.
```


```

### How it looks in the Command Interpreter

![](ls.png)

![](ejem_env_pwd_cd_exit.png)

### GLOSARY & IMPORTANT DEFINITIONS

#### PRIMAR

## Authors
* **Mariana Plazas** - [marianaplazas]
(https://github.com/marianaplazas)
* **Maria Alejandra Coy** - [macoyulloa]
(https://github.com/macoyulloa)
Please read [AUTHORS]
(https://github.com/marianaplazas/AirBnB_clone/tree/staging) or details on our code of conduct, and the process for submitting pull requests 
