#Task_1.1
my_list = [1, 2, 3]

def oops(i):
    print(my_list[i])


def oops_inside(i):
    try:
        oops(i)
    except IndexError:
        print("IndexError is present")

oops_inside(6)


#Task_1.2
my_dict = {'1': 'one', '2': 'two', '3': 'three'}

def oops(i):
    print(my_dict[i])


def oops_inside(i):
    try:
        oops(i)
    except IndexError:
        print("IndexError is present")

oops_inside(6)



#Task_2


def operation():
    try:
        a = float(input('Please, print a number A: '))
        b = float(input('Please, print a number B: '))
        result = (a**2)/b
        return result
    except ZeroDivisionError as z:
        print(f'Error is defined: {z}')
    except ValueError as v:
        print(f'Error is defined: {v}')


print(operation())
