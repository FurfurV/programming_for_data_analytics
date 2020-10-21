# Created by Viktoria 
# (▰˘◡˘▰)
# 21/10/2020
# Student number: R00180598

print("Welcome!")

qualification=int(input("How many years of experience you have?: "))

if(qualification>=4):
    certification=input("Do you have Microsoft qualification? yes/no: ")

    if(certification=="yes"):
        honours=input("Do you have first class honours undergraduate computing degree? yes/no: ")

        if(honours=="yes"):
            print("Congratulations, you are eligible")
        else:
            print("Sorry, you need first class honours")
    else:
        print("Sorry, need Microsoft qualifications")
else:
    print("Sorry, need more experience")
