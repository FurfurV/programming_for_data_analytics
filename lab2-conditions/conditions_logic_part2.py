# Created by Viktoria
# (▰˘◡˘▰)
# 03/10/2020
# Student number: R00180598

#Using conditional statements and logical operators write apython code that satisfies the following condition:
# If salary more than 40 or you are older than 35 and
# if you have worked 10 years or you have kid you can apply for mortgage.

salary40 = False
age35= False
work10 = True
kid = True

if salary40 | (age35 & work10) | kid:
    if True:
        print("You can apply")

else:
    print("cant apply")