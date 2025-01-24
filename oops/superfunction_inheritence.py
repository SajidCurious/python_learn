# super() is used in a subclass to call a method from its superclass, typically to extend or modify its behavior.

class Car:
    def __init__(self,type):
        self.type = type
    
    @staticmethod
    def start():
        print("car started")
    
    @staticmethod
    def stop():
        print("car stopped")

class ToyataCar(Car):
    def __init__(self, type,brand):
        super().__init__(type)
        self.brand = brand
        super().start()

s1 = ToyataCar("diesel","prius")
print(s1.type,s1.brand)