'''
Author:Elna Ann Bittaj
Date;8/11/2024
Description:to find largest and smallest from given list of numbers
'''
limit=int(input("enter the limit"))
number=int(input("enter a number"))
big=number
small=number
while limit>0:
    number=int(input("Enter a number"))
    if number>big:
        big=number
    elif number<small:
        small=number
    limit=limit-1
    print(f"big={big}")
    print(f"small={small}")





