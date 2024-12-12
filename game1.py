'''
Author: Elna Ann Bittaj
Date:15/11/2024
Description: Stone,Paper,Scissors Game
'''
import random
my_list=["rock,scissors,paper"]
user_choice=input("Enter rock,paper,scissors:")
comp_choice=random.choice(my_list)
if user_choice==comp_choice:
    print("its a tie!!")
elif user_choice=="rock" and comp_choice=="scissors":
    print("you won")
elif user_choice=="paper" and comp_choice=="rock":
    print("you won")
elif user_choice=="scissors" and comp_choice=="paper":
    print("you won")
else:
    print("you lost")