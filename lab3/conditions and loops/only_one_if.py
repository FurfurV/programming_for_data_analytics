# Created by Viktoria 
# (▰˘◡˘▰)
# 21/10/2020
# Student number: R00180598

qualification=int(input("How many years of experience you have?: "))
certification=input("Do you have Microsoft qualification? yes/no: ")
honours=input("Do you have first class honours undergraduate computing degree? yes/no: ")

if(qualification>=4 and certification=="yes" and honours=="yes"):
    print("Congratulations, you are eligible")

else:
    print("You are not eligible for this position.")

