# write a function to print the elements of a list in a single line using the loop

city = ["Hyd","BLR","DEL","KKR"]
state = ["TEL","KNR","DEL"]

def cal(list):
    for item in list:
        print(item, end=" ");

cal(city)