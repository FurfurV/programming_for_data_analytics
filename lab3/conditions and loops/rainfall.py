# Created by Viktoria 
# (▰˘◡˘▰)
# 21/10/2020
# Student number:

def rain_calculator():
    months=int(input("How many months of data to be entered: "))
    rain=[]
    if(months>12 or months<1):
        print("Sorry, numbers between 1 and 12 only")

    else:
        for i in range(months):
            value=float(input("Please enter rainfall for month {}: ".format(i+1)))
            rain.append(value)

        print("The average rainfall is: {}".format(sum(rain)/months))
        print("The lowest value is: {}".format(min(rain)))
        print("The highest value is: {}".format(max(rain)))

rain_calculator()