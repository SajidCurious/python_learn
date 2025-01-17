# class is a blueprint for the object
# object is an instance of the class

class Student:
    def __init__(self, fullname):
        self.name = fullname
        print("I'm winning the game")

s1 = Student("Sajid")
print(s1.name)

s2 = Student("Wajid")
print(s2.name)