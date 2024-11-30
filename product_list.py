'''author:Elna Ann Bittaj
date:30/11/2024
description:
description:Write a Python function to find product of all the numbers in a list'''
def product_of_list(list):
    product=1
    for i in list:
        product=product*i
    print(product)
list=[]
num=int(input("enter the number of elements:"))
for i in range(num):
    n=int(input("Enter the number:"))
    list.append(n)
print(list)
product_of_list(list)