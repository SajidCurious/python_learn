# Write a program to check if a list contains a palindrome of elements

list = [1,2,3,4,5]
copy_list = list.copy()
copy_list.reverse()

if(list == copy_list):
    print("It is a palindrome")
else:
    print("Not a palindrome")