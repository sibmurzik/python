#"Словари и множества"

#Работа со словарями
my_dict = {'Natalya': 1991, 'Andrey': 1974, 'Marina': 2000, 'Vasily': 2005}
print('Inital dictionary',my_dict)
print('Existing value:',my_dict.get('Andrey', 'Mentioned key is absent'))
print('Not existing value: ',my_dict.get('Artem', 'Mentioned key is absent'))

my_dict.update({'Mikhail': 2003, 'Albert': 1986})
#print(my_dict)
a= my_dict.pop('Natalya')
print("Value of key 'Nataly'", a)
print('Modified distionary ',my_dict)

#Работа с множествами
my_set = {1, 2, 3, 'Marina', 6.7 , 1, 2, False }
print('Initial set: ',my_set)

my_set.update({100, 200})
my_set.remove('Marina')
print('Modified set:', my_set)