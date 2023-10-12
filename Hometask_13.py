# Task_1
def func():
    a = 1
    c = 2
    e = "e"
    lst = [1, 2, 3]
    tpl = (2, 3, 4)
    dct = {"1": "2", "3": "4"}
    loc_var = locals()
    return len(loc_var)

num_func = func()
print(num_func)


# Task_2
def outer(x):
    def inner(y):
        return x + y
    return inner

outer_2 = outer(2)(3)
print(outer_2)


# Task_3
def choose_func(nums, func1, func2):
    if all(num > 0 for num in nums):
        return func1(nums)
    else:
        return func2(nums)

def func1(nums):
    return [num ** 2 for num in nums]

def func2(nums):
    return [num + 2 for num in nums]

numbers = [1, 2, 3, 4, 5]
print(choose_func(numbers, func1, func2))

numbers = [1, -2, 3, -4, 5]
print(choose_func(numbers, func1, func2))