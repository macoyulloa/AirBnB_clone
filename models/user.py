#!/usr/bin/python3
class User(BaseModel):
" class User that inherits from BaseModel "

    def __init__(self, email, password, first_name, last_name)
        " public class attributes " 
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
