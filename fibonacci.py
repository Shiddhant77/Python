'''
Write a Python program to generate the Fibonacci series up to a given number 'n'.

'''
import math

while True:
    n = int(input("Enter the nth number you like : "))
    if n < 1:
        continue
    else:
        break

a = 0
b = 1
sum = []

while len(sum) < n:
    sum.append(a)
    c = a + b
    a = b
    b = c
print(sum)