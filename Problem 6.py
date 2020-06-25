'''
Generate a random integer from a to b. You and your friend have to guess a number between two numbers a and b. 
a and b are inputs taken from the user. Your friend is player 1 and plays first. He will have to keep choosing
the number and your program must tell whether the number is greater than the actual number or less than the actual number.
Log the number of trials it took your friend to arrive at the number. You play the same game and then the person with minimum number of trials wins!

Randomly generate a number after taking a and b as input and don’t show that to the user (say 6)

Input:
Enter the value of a
4
Enter the value of b
13

Output:
Player1 :
Please guess the number between 4 and 13
5
Wrong guess a greater number again
8
Wrong guess a smaller number again
6
Correct you took 3 trials to guess the number
Player 2:
.
.
.

Correct you took 7 trials to guess the number
Player 1 wins!
'''
import random

a = int(input('Enter the min value: '))
b = int(input("Enter the max value: "))
print('\n')

c = random.randint(a, b)

trails1 = 0
p1 = ''
print("Player 1 turns...\n")
while p1 != c:
    p1 = int(input(f'Please enter the number between {a} and {b}.\n'))
    trails1 += 1
    if p1 == c:
        print(f'Correct! You took {trails1} trails to guess the number.\n')
    elif p1 < c:
        print('Worng guess. Enter a greater number.\n')
    elif p1 > c:
        print('Worng guess. Enter a smaller number.\n')

trails2 = 0
p2 = ''
print("Player 2 turns...\n")
while p2 != c:
    p2 = int(input(f'Please enter the number between {a} and {b}.\n'))
    trails2 += 1
    if p2 == c:
        print(f'Correct! You took {trails2} trails to guess the number.\n')
    elif p2 < c:
        print('Worng guess. Enter a greater number.\n')
    elif p2 > c:
        print('Worng guess. Enter a smaller number.\n')

if trails1 > trails2:
    print("PLayer 2 wins!")
else:
    print("Player 1 wins!")
