# class is a blueprint for the object
# object is an instance of the class

class Student:
    college = "SFBU"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("I'm winning the game")

s1 = Student("Sajid", 90)
print(s1.name, s1.marks, s1.college)

s2 = Student("Wajid", 50)
print(s2.name, s2.marks, s2.college)