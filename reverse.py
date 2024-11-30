'''author:Elna Ann Bittaj
date:30/11/2024
description:Write a Python program to reverse a string
'''
def reverse_of_string(string):
    return string[-1::-1]
x=input("Enter a string:")
print(reverse_of_string(x))