# Created by Viktoria 
# (▰˘◡˘▰)
# 21/10/2020
# Student number: R00180598
import math

def powerV1():
    num1=int(input("please enter the base number: "))
    num2=int(input("please enter the power number: "))
    print("The value {} raised to the power of {} is :{} ".format(num1,num2,pow(num1,num2)))

def powerV2():
    num1=int(input("please enter the power number: "))
    result=int(input("please enter the result number: "))
    print("The logarithm of {} with base {} is : {}".format(result,num1,math.log(result,num1)))


def main():
    powerV1()
    powerV2()

main()
