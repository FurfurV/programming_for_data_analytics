"""
Created on Sat Oct  3 10:52:07 2020
# Created by Viktoria
# (▰˘◡˘▰)
# Student number: R00180598
"""

my_tax = int(input("Please enter tax:"))
kids = input("have kids? y/n: ")
phrase = "Your tax is: "

if my_tax > 70:
    print(phrase, "55")
elif my_tax > 50:
    if kids == "y":
        print(phrase, "45")
    else:
        print(phrase, "50")
elif my_tax > 30:
    if kids == "y":
        print(phrase, "35")
    else:
        print(phrase, "40")
else:
    print(phrase, "0")
