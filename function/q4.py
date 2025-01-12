# write a function which takes a number input from the user and return "odd" if it is odd or return "even" if it is even.

def evaluator():
    value = int(input("Enter the value: "))
    if value%2 == 0:
        print("EVEN")
    else:
        print("ODD")

evaluator()
