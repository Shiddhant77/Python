'''
Write a Python program to implement the binary search algorithm. The program should take a sorted list of numbers and a target number as input and return
the index of the target number if found, or -1 if it is not present.
'''

list1 = [1,2,10,23,23,435,65,32,90,12,32,34,200,122,344,55]
list1.sort()

target = int(input("Enter the target number : "))
left = 0
right = len(list1)- 1

while left<=right:
    middle_ind = (left+right) //2
    if target == list1[middle_ind]:
        print(f"The target number {target} is in the {middle_ind} index position")
        break
    elif target < list1[middle_ind]:
        right = middle_ind - 1
    elif target > list1[middle_ind]:
        left= middle_ind + 1


if target not in list1:
    print("return 1")