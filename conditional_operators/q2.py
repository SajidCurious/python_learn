# write a program to check which is the bigger number from the three given inputs from the user

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if(a > b and a > c):
    print("First number is largest and it is ", a)
elif(b > a and b > c):
    print("Second number is the largest and it is ", b)
else:
    print("Third number is the largest and it is ", c)