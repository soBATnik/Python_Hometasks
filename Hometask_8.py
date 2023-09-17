# Task_1
def favorite_movie(name):
    print(f"My favorite movie is named {name}")
favorite_movie("Harry Potter")


# Task_2
def make_country(name, capital):
    country = {name: capital}
    print(country)
make_country('UK', 'London')


# Task_2.1
country = {"UK": "London", "US": "Washington"}
swap_country = {value: key for key, value in country.items()}
print(swap_country)


# Task_3
def make_operation(operator, *args):
    if operator == "+":
        print(sum(args))
make_operation("+", 2, 2)


# Task_3.1
def make_operation(operator, *args):
    result = float(args[0])
    if operator == "+":
        for num in args[1:]:
            result += float(num)
    elif operator == "-":
        for num in args[1:]:
            result -= float(num)
    elif operator == "*":
        for num in args[1:]:
            result *= float(num)
    elif operator == "/":
        for num in args[1:]:
            if float(num) == 0:
                return "Error: Division by zero"
            result /= float(num)
    return f'Result is: {result}'

print(make_operation("+", 2, 2, 2, 2))
print(make_operation("-", 2, 2, 2, 2))
print(make_operation("*", 2, 2, 2, 2))
print(make_operation("/", 2, 2, 2, 2))
