'''
Write a Python program to check if two given strings are anagrams or not.

'''

# its like  jumble word  ==== cinema ==> iceman

#
# word = input("Enter the word you like : ")
#
# word_s = input("Enter another word you like : ")
#
# common_word = []
# if len(word) != len(word_s):
#     print("The given strings are not anagrams")
# else:
#     for i in range(len(word)):
#         for j in range(len(word_s)):
#             if word[i] == word_s[j]:
#                 common_word.append(word_s[j])
#             if j <(len(word)-1):
#                 j =j+1
#             else:
#                 pass
#         i = i+1
#
# for num in common_word:
#     print(num, end='')
# if word == num:
#     print("The words are anagram!")
#----------------------------------------------------------------------------------------------------------------------------------
# Above was my logic which I took my time doing, but still could be fully correct
# Internet code

word = input("Enter the first word: ")
word_s = input("Enter the second word: ")

if sorted(word.lower()) == sorted(word_s.lower()):
    print("The words are anagrams!")
else:
    print("The words are not anagrams.")