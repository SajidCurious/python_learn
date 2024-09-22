# Take an input from the user and write a program. If the input is above 18 he or she can vote.

age = int(input("Enter your age: "))
if(age >= 18):
    print("You can vote")
else:
    print("You cannot vote")