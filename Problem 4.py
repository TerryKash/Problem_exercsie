'''
A palindrome is a string which when reversed is equal to itself:

Examples of palindrome includes 616, mom, 676, 100001

You have to take a number as an input from the user. You have to find the next palindrome corresponding to that number. 
Your first input should be ‘number of test cases’ and then take all the cases as input from the user


Input:

3
451
10
2133

Output:

Next palindrome for 451 is 454

Next palindrome for 10 is 11

Next palindrome for 2133 is 2222
'''

def reverse(num):
    n = str(num)
    r = n[::-1]
    return r

n = int(input("How many numbers you want to check? "))
for i in range(n):
    num= int(input("Enter any number :- "))
    if str(num)==reverse(num):
        print ("Already palindrome.")
    else:
        while True:
            num+= 1
            if str(num)==reverse(num):
                print(f"Next palindrome is {num}")
                break