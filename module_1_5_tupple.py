#"Неизменяемые и изменяемые объекты. Кортежи"

immutable_var = (1, 2, 3, True, "sun", 87, 76.8)
print(immutable_var)

#immutable_var[1] = 8

#При попытке присвоить другое значение элементу кортежа получаем ошибку
# TypeError: 'tuple' object does not support item assignment
#так как кортеж это неизменяемая последовательность элементов

mutable_list = [1, 2, 3, True, "sun", 87, 76.8]
mutable_list[2:3] = [9, False]
print(mutable_list)

