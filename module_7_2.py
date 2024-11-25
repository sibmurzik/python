# "Позиционирование в файле"

def custom_write(file_name, strings):
    file = open(file_name, 'w')
    file.close()
    file = open(file_name, 'a', encoding='utf-8')
    strings_positions = dict()
    index = 1
    for i in strings:
        strings_positions[str(index) + ',' + str(file.tell())] = i
        file.write(str(i) + ' \n')
        index += 1
    file.close()
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
