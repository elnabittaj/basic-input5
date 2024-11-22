'''
Author:Elna Ann Bittaj
Date:22-11-2024

'''
list_1=[1,2,3,4]
list_2=[5,6,7,8]
list_3=list_1+list_2
print(list_1)
print(list_2)
print(list_3)
even_list=[]
odd_list=[]
for number in list_3:
    if number%2==0:
        even_list.append(number)
        even_list.sort(reverse=True)
    else:
        odd_list.append(number)
        odd_list.sort(reverse=True)
print(even_list+odd_list)