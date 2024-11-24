# "Режимы открытия файлов"

import os.path

class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}.'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        if  not os.path.exists(self.__file_name):
            file = open(self.__file_name, 'w')
            file.close()

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        inventory = self.get_products()
        file = open(self.__file_name, 'a')
        for i in products:
            if str(i) not in inventory:
                file.write('\n' + str(i))
            else:
                print(f"Продукт {i} уже есть в магазине")
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)  # __str__
s1.add(p1, p2, p3)
print(s1.get_products())
