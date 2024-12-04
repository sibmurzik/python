#"Сложные моменты и исключения в стеке вызовов функции"

def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError as exc:
            incorrect_data += 1
            #print(f"Error {exc}")
    return (result, incorrect_data)

def calculate_average(numbers):
    try:
        res_tuple = personal_sum(numbers)
        return res_tuple[0] / (len(numbers) - res_tuple[1])
    except ZeroDivisionError as exc:
        #print(f'Error:  {exc}')
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать


