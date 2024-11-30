'''author:Elna Ann Bittaj
date:30/11/2024
description:
description:Write a Python function to sum all the numbers in a list'''
def sum_of_list(list):
    sum=0
    for i in list:
        sum=sum+i
    print(sum)
list=[]
num=int(input("enter the number of elements:"))
for i in range(num):
    n=int(input("Enter the number:"))
    list.append(n)
print(list)
sum_of_list(list)
