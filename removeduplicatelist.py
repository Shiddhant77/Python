'''
Write a Python program to remove duplicates from a given list.

'''

list1 = [1,1,1,1,2,3,4,545,32,234,2,3,4,4,4,5,2,3,4,5]

unique = []

for num in list1:
    if num not in unique:
        unique.append(num)

print(unique)
