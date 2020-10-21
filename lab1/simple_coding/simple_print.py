"""
Created on Wed Sep 30 09:19:00 2020
# Created by Viktoria
# (▰˘◡˘▰)
# Student number: R00180598
"""

newNum=0

#question 4

name=input("Enter your name")

surname=input("Enter your surname")

for i in range(3):
    num=int(input("Enter your grade"))
    newNum+=num
    #print(newNum)
    
print(name,surname,newNum/3)
    
