# Input
# Input refers to data provided to a Python program, typically by the user, which the program processes. In Python, the input() function is used to accept input from the user.
# The input() function reads data as a string. To work with other data types, the input needs to be converted (e.g., using int() or float()).

# Output
# Output refers to the data or information that a Python program produces and displays to the user or writes to a file. The print() function is commonly used for output in Python.
# Output can also be formatted for readability using techniques like f-strings or .format().

f = open("sajid.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()

# If we just wanted to retrieve the specific characters from the imported file, we should add the characters to the read function.

f = open("sajid.txt","r")
data = f.read(6)
print(data)
f.close()