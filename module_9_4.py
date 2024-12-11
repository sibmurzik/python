# "Создание функций на лету"

from random import choice

# Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y, first, second)))


# Замыкание:
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w') as file:
            for i in range(len(data_set)):
                if isinstance(data_set[i], str):
                    element = "'" + data_set[i] + "'"
                else:
                    element = str(data_set[i])
                file.write(element)
                if i != len(data_set) - 1:
                    file.write(',')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Метод __call__:
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное', 8)

print(first_ball())
print(first_ball())
print(first_ball())
first_ball = MysticBall(7)
print(first_ball())
