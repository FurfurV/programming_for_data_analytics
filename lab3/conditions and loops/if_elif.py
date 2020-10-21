# Created by Viktoria 
# (▰˘◡˘▰)
# 21/10/2020
# Student number: R00180598

price=99
discount=0

package_num=int(input("How many packages? :"))

if(package_num<=0):
    print("Should be greater than 0")

elif(package_num>=10 and package_num<=19):
    discount=0.2

elif(package_num>=20 and package_num<=49):
    discount=0.3

elif(package_num>=50 and package_num<=99):
    discount=0.4

elif(package_num>=100):
    discount=0.5

calculate=package_num*price

print('The total price: {} with discount: {}'.format(calculate,calculate*discount))
