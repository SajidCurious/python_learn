# Inheritance in object-oriented programming (OOP) is a mechanism where one class (called the child or subclass) can inherit properties and behaviors (fields and methods) from another class (called the parent or superclass). It allows code reuse, establishes a relationship between classes, and supports the principles of modularity and extensibility.

class Car:
    @staticmethod
    def start():
        print("car has started")

    @staticmethod
    def stop():
        print("Car has stopped")

class ToyataCar(Car):
    def __init__(self,brand):
        self.brand = brand

class Fortuner(ToyataCar):
    def __init__(self,type):
        self.type = type

s1 = Fortuner("Diesel")
s1.start()