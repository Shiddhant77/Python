'''
Write a Python program to check if a given number is prime or not.

'''



while True:
    n = int(input("Enter the number you like : "))
    if n < 1:
        continue
    else:
        break



i = 2

while i<=n:
    if n % i ==0 and n==i:
        print("The number is prime")
        break
    elif n % i == 0 and n!=i:
        print("The number is not prime")
        break
    else:
        i+=1


