'''
You are given a list which contains some numbers. 
You have to print a list of next palindromes only if the number is greater than 10 otherwise you will print that number.

Input:
[1, 6, 87, 43]

Output:
[1, 6, 88, 44]
'''

my_list = []
n = int(input('How many number you wanna take in a list: '))
for i in range(n):
    num = int(input(f'Enter the {i+1} number: \n'))
    my_list.append(num)
print('Your list:')
print(f"{my_list}\n")

new_list = []
for numb in my_list:
    if numb < 10:
        new_list.append(numb)
    else:
        while str(numb) != str(numb)[::-1]:
            numb += 1
        new_list.append(numb)
print('Palindrome list(if number greater than 10):')
print(f"{new_list}\n")
