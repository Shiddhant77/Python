'''
Palindrome Checker: Develop a program that checks if a given string is a palindrome (reads the same forward and backward)
. Ignore whitespace and punctuation in the check.
'''
import string
from string import punctuation

user_input = input("Enter the string you like : ").replace(" ",'')

user_input = user_input.translate(user_input.maketrans('','', punctuation))



if user_input[0::] == user_input[::-1]:
    print("The string is palindrome")
else:
    print("The string is not palindrome")

