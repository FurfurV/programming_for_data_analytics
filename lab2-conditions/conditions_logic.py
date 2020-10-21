# Created by Viktoria
# (▰˘◡˘▰)
# 03/10/2020
# Student number: R00180598

# Using conditional statements and logical operators write a python code that satisfies the following condition:
#
# If salary more than 40 and you are older than 25 or
# if you have worked 25 years and have kid you can apply for mortgage.


salary40 = False
age25 = False
work25 = True
kid = True

if (salary40 & age25) | (work25 & kid):
    if True:
        print("You can apply")
else:
    print("cant apply")

