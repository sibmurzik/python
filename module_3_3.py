#"Распаковка позиционных параметров"
# 1.Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params()
print_params(c = 10)
print_params('andrey', 8)
print_params('string', 'string','string')

print_params(b = 25)
print_params(c = [1,2,3])

#2.Распаковка параметров:
values_list = ["list_value", 10, False]
values_dict = {'a':10, 'b':True, 'c':'dict_value'}

print_params(*values_list)
print_params(**values_dict)

#Распаковка + отдельные параметры:
values_list_2 = ['list2', 55]
print_params(*values_list_2, 42)


