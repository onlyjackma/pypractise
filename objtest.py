#!/usr/bin/env python
class Human(object):
    Can_Talk = True
    Can_Walk = True
    Age = 0
    Name = ["Li", "Lei"]


a = Human()
b = Human()

a.Age += 1
print a.Age
print b.Age

a.Name[0] = "Wang"
print a.Name
print b.Name

