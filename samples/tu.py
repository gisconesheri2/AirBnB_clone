#!/usr/bin/python3

from models.user import User

u1 = User()
u1.first_name = "popo"
tr = u1.to_dict()

u2 = User(**tr)
print(u2)

u3 = eval("BaseModel")
