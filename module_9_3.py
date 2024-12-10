#"Генераторные сборки"

first = ['Strings', 'Student', 'Computers', 'Table']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = ( len(x)-len(y) for x, y in zip(first, second) if len(x) != len(y))
second_result = ( len(first[i])== len((second[i])) for i in
                  range(len(first) if len(first) <= len(second) else len(second)))

print(list(first_result))
print(list(second_result))