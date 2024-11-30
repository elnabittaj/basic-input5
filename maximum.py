author:Elna Ann Bittaj
date:30/11/2024
description: Write a Python function to find the maximum of three numbers.

def max_of_numbers(list):
    list.sort()
    print("maximum value is:",list[2])
num1=int(input("Enter a number"))
num2=int(input("Enter a number"))
num3=int(input("Enter a number"))
list=[num1,num2,num3]
max_of_numbers(list)

