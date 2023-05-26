'''
Password Generator: Create a program that generates random passwords of a specified length. Allow the user to customize
the password length and choose whether to include uppercase letters, lowercase letters, numbers, and special characters.


'''
import random
i =0
password_length = int(input("Enter the length of the password : "))
if password_length<8:
    print("Please enter password with more than 8 character")

else:

    word = 'abcdefghijklmnopqrstuvwxyz'
    words = word.upper()
    number = '0123456789'
    special_char = '!@#$%^&*()'



    customize = input("Do you want to add any special characters : ")

    if customize.upper() == 'YES':
        while(i!=password_length):
            new_word = word + words + number+ special_char
            new_word = random.choice(new_word)
            print(new_word, end='')
            i+=1

    elif customize.upper() == 'NO':
        while(i!=password_length):
            new_word= word+ words+ number
            new_word = random.choice(new_word)
            print(new_word, end='')
            i+=1
