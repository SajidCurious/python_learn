# Abstraction in programming is the process of simplifying complex systems by focusing on the essential details while hiding unnecessary complexities.

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car Started")


s1 = Car()
s1.start()