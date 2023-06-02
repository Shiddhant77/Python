'''
Write a Python program that allows the user to play Rock, Paper, Scissors against the computer.

'''
import random
g = input("Enter, R for Rock, P for Paper, or S for Scissors ").upper()
comp_choice = ['R','P','S']
c = random.choice(comp_choice)
c = c.upper()



if g == c:
    print("Draw")
elif g == 'R' and c == 'S':
    print("You Win")
elif g == 'P' and c == 'R':
    print("You Win")
elif g == 'S' and c == 'P':
    print("You Win")
else:
    print("Computer wins")
print(c)