''''
Take age or year or birth as an input from the user and tell them when they will turn 100 years old.(5 points)
Don’t use any type of module like datetime or dateutils(-5 points).

They can then optionally provide a year and your program must tell their age in that particular year. (3 points)
You should be handling all sorts of errors like (2 points):
    -You are not yet born
    -You seem to be the oldest person alive
    -You can also handle any other error if possible!
'''

print("#*#*#*THIS IS A AGE CALCULATOR*#*#*#")

i = ""
while i != "q":

    user_input = input("Enter you age or year of birth: ")
    if (len(user_input) == 4 and int(user_input) > 2020) or (len(user_input) == 2 and int(user_input) < 0) :
        print("You are not born yet!\nPlease enter a valid year or age.")

    elif len(user_input) == 4 and int(user_input) < 1900:
        age = 2020 - int(user_input)
        print(f"Your age is: {age}.")
        print("You'r the oldest person alive!!")

    elif  int(user_input) > 120 and len(user_input) == 3:
        age = int(user_input)
        print("You'r the oldest person alive!!")

    elif len(user_input) == 4:
        age = 2020 - int(user_input)
        print(f'Your age is {age}.')
        age2 = 100 - age
        year = age2 + 2020
        print(f'You will turn 100 in year {year}.')

    elif len(user_input) == 2:
        age = int(user_input)
        age2 = 100 - age
        year = age2 + 2020
        print(f'You will turn 100 in year {year}.')

    i = input("Press 'c' to continue and 'q' to quit.")