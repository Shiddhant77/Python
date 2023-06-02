'''
Write a Python program to reverse a given string without using any built-in reverse functions or slicing.

hello ==> olleh

'''


user_input = input("Enter a string you like : ")

for i in range(len(user_input)):
    if i == (len(user_input)-1):
        while i >= 0:
            print(user_input[i], end='' )
            i = i -1
    else:
        i = i+1
