"""
Created on Wed Oct  7 14:33:21 2020
# Created by Viktoria
# (▰˘◡˘▰)
# Student number: R00180598
"""
# =============================================================================
# 
# The area of a rectangle is the length multiplied by width.
#  Write a program that asks for the length and width of two rectangles. 
#  The program should tell the user which rectangle has the greater area or
#  if the areas are the same
# =============================================================================

#area=length*width


try:
    print("Enter triangle 1:")
    length1 = int(input("Enter length:"))
    width1 = int(input("Enter length:"))
    area1 = length1 * width1

    print("Enter triangle 2:")
    length2 = int(input("Enter length:"))
    width2 = int(input("Enter length:"))

    area2 = length2 * width2

    if(area1>area2):
        print("First triangle has bigger area:", area1)
    elif(area2>area1):
        print("Second triangle has bigger area:", area2)
    else:
        print("They have the same area.")


except ValueError:
    print("Only whole numbers please")

