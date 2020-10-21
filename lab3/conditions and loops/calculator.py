# Created by Viktoria 
# (▰˘◡˘▰)
# 21/10/2020
# Student number: R00180598

options=["Addition","Subtraction","Multiplication","Division"]
symbols=['+','-','*','/']

def menu():
    print("What would you like to perform?")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")


def calculate(num1, num2, choice):
    if (choice == 1):
        final = num1 + num2
        return final

    elif (choice == 2):
        final = num1 - num2
        return final

    elif (choice == 3):
        final = num1 * num2
        return final
    else:
        final = num1 / num2
        return final

def smallcalc(num1,num2,choice):
    if(choice>=1 and choice<=4):
        total = num1 + symbols[choice - 1] + num2
        return eval(total)

def main():
    num1 = int(input("Please enter a numerical value: "))
    num2 = int(input("Please enter another numerical value: "))
    menu()
    choice = int(input("> "))
    final = calculate(num1, num2, choice)

    print("{} of {} and {} is {} ".format(options[choice-1],num1, num2, final))
    print("{:-^40}".format(""))
    final2 = smallcalc(str(num1), str(num2), choice)
    print("{} of {} and {} is {} ".format(options[choice - 1], num1, num2, final2))

main()
