"""
Created on Wed Sep 30 09:37:26 2020
# Created by Viktoria
# (▰˘◡˘▰)
# Student number: R00180598
"""

ticketA=int(input("How many class A tickets? "))
ticketB=int(input("How many class B tickets? "))
ticketC=int(input("How many class C tickets? "))

ticketB*=20
ticketA*=25
ticketC*=30

income=ticketA+ticketB+ticketC

print("Income generated: ", income)

