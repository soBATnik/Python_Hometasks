# Task_1
import random
while True:
    gen_number = random.randint(1, 10)
    user_number = int(input('Enter your number (1-10), or enter 0 to quit: '))
    if user_number == 0:
        print('Thanks for playing!')
        break
    elif user_number in range(1, 11):
        if gen_number == user_number:
            print('High five!')
        else:
            print('Alas...')
    else:
        print('Please enter a number between 1 and 10.')

#Task_2
user_name = input("Hello! Print your name, please: ")
user_age = int(input("And enter your age: "))
user_age_next_year = str(user_age + 1)
print('Hello, ' + user_name + ", " + "you're " + str(user_age) + ". " + "Next year you'll be " + user_age_next_year + ".")

#Task_3
import random

while True:
    user_str = input("Enter your word or 'exit' to quit: ").lower()

    if user_str == 'exit':
        print('Bye')
        break
    elif user_str.isalpha():
        user_list = list(user_str)
        for _ in range(5):
            random.shuffle(user_list)
            print(''.join(user_list))
    else:
        print('Try again')