# Created by Viktoria 
# (▰˘◡˘▰)
# 21/10/2020
# Student number: R00180598

fibonacci=[0,1]

def sequence():
    for i in range(40+1):
        fibonacci.append(fibonacci[i]+fibonacci[i+1])
    print(fibonacci)

def getNum(index):
    return fibonacci[index-1]

sequence()
print(getNum(13))
