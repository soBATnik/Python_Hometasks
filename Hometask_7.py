# Task_1
user_input = str(input("Print something: ").lower()).split()
user_dict = {}
for word in user_input:
    if word in user_dict:
        user_dict[word] += 1
    else:
        user_dict[word] = 1

result_dict = str(user_dict)
print(result_dict)


# Task_2
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

sum_prices = {key: stock[key] * prices[key] for key in stock if key in prices}
sum_money = sum(sum_prices.values())
print(sum_money)


# Task_3
i_list = []
j_list = []
for i in range(1, 11):
    i_list.append(i)
    j_list.append(i ** 2)
i_tuple = set(i_list)
j_tuple = set(j_list)

comprehension_list = [item for tuple_items in (i_tuple, j_tuple) for item in tuple_items]
print(comprehension_list)


# Task_4
normal_days_of_week = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
swap_days = {value: key for key, value in normal_days_of_week.items()}
print(swap_days)