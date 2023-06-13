'''
Write a Python program to find the second largest number in a given list.

'''

list1 = [1, 2, 3, 4, 562, 42, 32444, 543, 234, 23424, 54436, 23432, 3245435, 5363, 23332, 3425356, 5]

largest_num = int()   # place holders
second_largest = int() # place holders

for num in list1:
    if num > largest_num: # checking if the num is greater that largest number
        second_largest = largest_num # if yes then the largest number becomes second largest
        largest_num = num # and the num becomes the largest number
    # it is done to ensure that second largest number is updated
    # if largest is 12 and currently our second largest is 10 and we encounter 11 then this condition will be executed and second largest is updated to 11
    elif num > second_largest and num!= largest_num: # again checking if another number is greater than current second biggest number and is not equal to current largest
        second_largest = num

print(second_largest)
print(largest_num)


