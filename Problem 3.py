'''
You visit a restaurant called CodeWithHarry and food items in this restaurant are sorted based on their amount of calories. 
You have to reverse this list of food items containing their calories.
You have to use following three methods to reverse a list:

• Inbuilt method of python
• Listname[::-1] slicing trick
• Swapping first element with last one and second element with second last one and so on….
Input:
Take a list as an input from the user.
[5,4,1]

Output:
[1,4,5]
[1,4,5]
[1,4,5]
All the three methods give same results
'''

a = list()

while True:
    user_input = input("Enter the value of calories or 'q' to quit: ")
    if user_input == "q":
        break
    a.append(user_input)

print("Original list: ", a)
print("Reversed list using slicing method: ", a[::-1])

reverse1 = a[:]
reverse1.reverse()
print("Reversed list using Inbulid function: ", reverse1)


def swapping_char():
    b = len(a)
    for i in range(b//2):
        a[i], a[b-i-1] = a[b-i-1], a[i]
        # b = b - i
    print("Reverse list using Swapping method", a)


swapping_char()
