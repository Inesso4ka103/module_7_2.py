from pprint import pprint
import io

def custom_write(file_name, strings):
    strings_positions = {}
    with open('file_name', 'w', encoding = 'utf-8') as my_file:
        for count, string in enumerate(strings, ):
            count += 1
            position = my_file.tell()
            strings_positions[(count, position)] = string
            my_file.write(string + '\n')
        return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)