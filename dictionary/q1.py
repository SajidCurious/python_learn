# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary and add one by one. Use subject name as key and marks as value.

marks = {}
a = int(input("Enter your Physics marks: "))
b = int(input("Enter your Bio marks: "))
c = int(input("Enter your Maths marks: "))

marks.update({"Physics" : a})
marks.update({"Bio" : b})
marks.update({"Maths" : c})
print(marks)