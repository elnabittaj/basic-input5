'''
Write a Python program that takes a single
character as input from the user and checks if it is a vowel or a consonant.
If the input is not an alphabetic character, print "Invalid input."
'''
char=input("Enter a single character: ")
if char.isalpha():
    if char in 'AEIOUaeiou':
        print(f"{char} is a vowel")
    else:
        print(f"{char} is a consonant")
ele:
    print("invalid input")