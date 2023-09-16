#Task 1

import random

random_number_list = list(random.randint(1, 20) for _ in range(10))
max_number = max(random_number_list)
print(str(random_number_list) + '. The max number from the list is ' + str(max_number))

#Task 1.2

import random
random_number_list = list(random.randint(1, 30) for _ in range(10))
max_number = random_number_list[0]
i = 1

while i < len(random_number_list):
    if max_number < random_number_list[i]:
       max_number = random_number_list[i]
    i += 1
print(str(random_number_list) + ' The max number is: ' + str(max_number))


#Task 2

import random
first_list = []
second_list = []

i = 0
while i < 10:.
    first_random_number = random.randint(1, 10)
    second_random_number = random.randint(1, 10)
    first_list.append(first_random_number)
    second_list.append(second_random_number)
    i += 1

print(str(first_list) + ' ' + str(second_list))
third_list = list(set(first_list + second_list))
print(str(third_list))


#Task 3

first_list = list(range(1, 100))
second_list = []
i = 0
while i < len(first_list):
    number = first_list[i]
    if number % 7 == 0 and i % 5 != 0:
        second_list.append(number)
    i += 1
print(str(second_list))