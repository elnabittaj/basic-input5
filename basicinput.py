'''
Author:Elna Ann Bittaj
Date:19-10-2024
Description:Simple desktop calculator using Python. Only the five basic arithmetic operators.
'''
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
sum=num1+num2
print("The sum of num1 and num2 is:",sum)
difference=num2-num1
print("The difference when num2 is subtracted from num1 is:",difference)
product=num1*num2
print("The product of num1 and num2 is:",product)
quotient=num1/num2
print("The quotient when num1 is divided by num2 is:",quotient)
remainder=num1%num2
print("The remainder when num1 is divided by num2 is:",remainder)
result=(num1+num2)*num3/2
print("The result of (num1 + num2) * num3 / 2 is:",result)