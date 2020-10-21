# Created by Viktoria 
# (▰˘◡˘▰)
# 21/10/2020
# Student number: R00180598

#i
def timetable():
    num=int(input("Enter value: "))

    limit=int(input("Limit to stop at: "))

    for i in range(limit +1):
        print("{}*{} = {}".format(num,i,i*num))


#ii
def printNumTriangle():
    size=int(input("Enter int for triangle size: "))

    for i in range(size+1):
        # print("")
        for s in range(i):
            print(i,end="")
        print("")


# timetable()
# printNumTriangle()
