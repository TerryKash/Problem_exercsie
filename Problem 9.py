'''
Funny Names
Its result day at school and not everyone is happy. You decided to make your friends laugh by jumbling their names to come up with some funny names.
Your program should take the number of names and the names separated by space as input. Output should be funny names in the same order.

Input:
Enter number of friends:
3

Enter the name of your 3 friends:
Rohan Das
Shubham Agarwal
Ritesh Arora

Output:
Ritesh Das
Shubham Arora
Rohan Agarwal
'''
import random


def list_generator(n):
    name_list = []
    for i in range(n):
        name = input(f"Enter the {i+1} name: ")
        name_list1 = name.split(" ")
        name_list.extend(name_list1)
        
    return name_list


def jumblingNames(list):
    seperate =' '
    


if __name__ == "__main__":
    n = int(input("How many names do you have"))
    print(list_generator(n))