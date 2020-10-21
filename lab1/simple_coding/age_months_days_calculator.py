"""
Created on Wed Sep 30 11:14:15 2020
# Created by Viktoria
# (▰˘◡˘▰)
# Student number: R00180598
"""

name=input("Enter your name please: ")
age=int(input("Enter your age: "))

months=age*12
days=age*365

print(name, " is ", months, " months old.")
print("%s is %d days old." % (name, days))