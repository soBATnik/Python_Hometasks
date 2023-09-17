print('mymod.py')


def count_lines(name):
    with open(name, 'r') as file:
        lines = file.readlines()
        print(len(lines))

def count_chars(name):
    with open(name, 'r') as file:
        chars = file.read()
        print(len(chars))

def test(name):
    count_chars(name)
    count_lines(name)
