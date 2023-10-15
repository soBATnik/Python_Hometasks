# Task_1
def decorator(func):
    def wrapper(*args):
        arg_str = ", ".join(map(repr, args))
        print(f"{func.__name__} called with {arg_str}")
    return wrapper

@decorator
def add(x, y):
    return x + y

@decorator
def squares(*args):
    return [arg ** 2 for arg in args]

add(2, 2)
squares(1, 2, 3, 4)


# Task_2
def rep_decorator(replacements):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, *kwargs)
            for old_word, new_word in replacements.items():
                result = result.replace(old_word, new_word)
            return result
        return wrapper
    return decorator

@rep_decorator({"pepsi": "*", "BMW": "*"})
def moto(name):
    return f"{name} drinks pepsi in his brand new BMW"

name_person = "Steve"
result = moto(name_person)
print(result)


# Task_3
def arg_decorator(max_length=15, type_ ='str', lst=[]):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if len(args) <= max_length:
                if type_ == 'str':
                    if all(char in args[0] for char in lst):
                        return func(*args, **kwargs)
                    else:
                        print("Argument doesn't contain any symbols from the list")
                else:
                    print('Not a string')
            else:
                print("Argument is too long")
            return False
        return wrapper
    return decorator

@arg_decorator(max_length=15, type_='str', lst = ["a", "b"])
def moto(name):
    return f"{name} drinks pepsi in his brand new BMW"

person_name = "Abba"
print(moto(person_name))