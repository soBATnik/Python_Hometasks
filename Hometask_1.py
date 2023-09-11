my_string = input("Введите слово")
result = my_string[:2] + my_string[-2:]
if len(result) > 2:
    print(result)
else:
    print('')


my_string = input('Введите слово')
result = my_string[:2] + my_string[-2:]
print(result if len(result) > 2 else '')