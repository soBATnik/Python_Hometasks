import os

file_dir = 'C:/Users/Yurii/PycharmProjects/pythonProject/HW9'
file_path = os.path.join(file_dir, 'task_3.txt')

with open(file_path, 'w') as file:
    file.write('The “sys.path” list is initialized from the PYTHONPATH\n'
               ' environment variable. Is it possible to change it from\n'
               ' within Python? If so, does it affect where Python looks\n'
               ' for module files? Run some interactive tests to find it out.\n'
               )

with open(file_path, 'r') as file:
    content = file.read()
    print(content)

from mymod import *

test('task_3.txt')
