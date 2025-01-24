# A class method in Python is a method that belongs to the class rather than any specific instance. It can access and modify the class's state but cannot directly modify instance-specific data. Class methods are defined using the @classmethod decorator, and their first parameter is conventionally named cls (referring to the class itself).

class Person:
    name = "Anonymous"

    @classmethod
    def changeName(cls,name):
        cls.name = name

p1 = Person()
p1.changeName("Sajid")
print(p1.name)
print(Person.name)