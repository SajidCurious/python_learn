# Private attributes cannot be accessed outside of the class

class Person:
    def __init__(self,account,password):
        self.account = account
        self.__password = password

    def get_password(self):
        print(self.__password)
        

s1 = Person(123456,"afjafjoa")
print(s1.get_password())
