# Search a specific number from the given data of the tuple

tup = (1,2,3,4,5,6,7,8,9,10)
x = 6
i = 0
while i < len(tup):
    if(tup[i] == x):
        print("Found at index",i)
    i += 1