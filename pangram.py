'''
Write a Python program to check if a given string is a pangram (a sentence containing every letter of the alphabet at least once).

'''

import  string


def is_pangram(sentence):
    sentence = sentence.lower()  #  converting given input to lower case
    sentence = sentence.translate(str.maketrans("", "", string.punctuation + " ")) # removing any punctuation and whitespace
    unique_char = set(sentence) # only adding unique set of elements inside the unique char
    alphabet = set(string.ascii_lowercase) # making alphabet also set cause we cannot compare set and string so alphabet is converted to set
    if alphabet == unique_char:
        print("The string is pangram")
    else:
        print("The string is not pangram")
    return sentence

user_input = input("Enter a string you like :")

pan = is_pangram(user_input)

