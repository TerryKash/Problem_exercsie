'''
Rohan Das Is A Fraud:

Rohan das is a fraud by nature.
Rohan Das wrote a python function to print a multiplication table of a given number and put one of the values (randomly generated) as wrong.
Rohan Das did this to fool his classmates and make them commit a mistake in a test. You cannot tolerate this!
So you decided to use your python skills to counter Rohan’s actions by writing a python program that validates Rohan’s multiplication table.
Your function should be able to find out the wrong values in Rohan’s table and expose Rohan Das as a fraud.
Note: Rohan’s function returns a list of numbers like this

Rohan Das’s Function Input:
rohanMultiplication(6)

Rohan’s function returns this output:

[6, 12, 18, 26, …., 60]

You have to write a function isCorrect(table, number) and return the index where rohan’s function is wrong and print it to the screen! 
If the table is correct, your function returns None
'''

import random

def rohanMultiplication(n):
    table1 = [i*n for i in range(1, 11)] 
    table1[random.randint(0, 10)] = random.randint(1, 60)
    return table1
        

def myMultiplication(n):
    table2 = [i*n for i in range(1, 11)]
    return table2


def isCorrect(table1, table2):
    for ind in range(0, 10):
        if table1[ind] == table2[ind]:
            # print(f'{ind+1} index is correct')
            continue
        else:
            print(f'There is something wrong at index {ind} in rohan multiplication table')


if __name__ == "__main__":

    n = int(input("Enter the value: \n"))
    print("Rohan Multipliation Table")
    print(rohanMultiplication(n), "\n")
    print("Correct Multipliation Table")
    print(myMultiplication(n), "\n")
    isCorrect(rohanMultiplication(n), myMultiplication(n))
