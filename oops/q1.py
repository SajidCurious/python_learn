#  Create a student class that makes name and marks of 3 subjects as arguments in consrtuctor.
#  Then create a method to print an average

class Student:
    college = "SFBU"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("HI", self.name , "Your average score is:", sum/3)


s1 = Student("Sajid",[50,60,70])
s1.average()

s2 = Student("Wajid",[10,90,20])
s2.average()

s3 = Student("Majid",[20,50,30])
s3.average()
