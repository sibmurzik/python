# Дополнительное практическое задание по модулю*
from math import pi, sqrt, pow


class Figure():
    sides_count = 0

    def __init__(self, color, *sides, filled=False):
        self.__color = (0, 0, 0)
        list_color = []
        if not isinstance(color, (tuple, list)):
            list_color.append(color)
        else:
            list_color = [*color]
        temp_color = []
        for i in range(3):
            if i < len(list_color):
                temp_color.append(list_color[i])
            else:
                temp_color.append(0)
        self.set_color(*temp_color)
        self.__sides = []
        if len(sides) == 1:
            self.__sides = [sides[0]] * self.sides_count
        elif len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
            # если размереы сторон не передаются то по умолчанию они все будут равны 1 
        else:
            for i in sides:
                if isinstance(i, int) and i > 0:
                    self.__sides.append(i)

        self.filled = bool(filled)
        #print(self.__color)
        #print(self.__sides)
        #print(self.filled)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            return r >= 0 and r <= 255 and g >= 0 and g <= 255 and b >= 0 and b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *new_sides):
        if len(self.__sides) != len(new_sides):
            return False
        for side in new_sides:
            if not isinstance(side, int) or side <= 0:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        sum = 0
        for i in self.__sides:
            sum += i
        return sum

    def set_sides(self, *new_sides):
        if len((new_sides)) != self.sides_count:
            return
        if self.__is_valid_sides(*new_sides):
            self.__sides = []
            for i in new_sides:
                self.__sides.append(i)
           
           
           


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides, filled=False):
        super().__init__(color, *sides, filled=filled)
        self.__radius = round(self.get_sides()[0] / (pi * 2), 3)
        #print(self.__radius)

    def get_square(self):
        return round(self.__radius ** 2 * pi, 3)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides, filled=False):
        super().__init__(color, *sides, filled=filled)

    def get_square(self):
        p = len(self) / 2
        # print(p)
        sides = self.get_sides()
        return round(sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])), 3)


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides, filled=False):
        # Куб обладает равними сторонами по определению
        # Если будут введены 12 разных значений граней то им присвоится значение пкрвой грани
        cube_sides = sides
        if len(sides) == self.sides_count:
            cube_sides = [sides[0]] * self.sides_count
            print("your entered different side's value for cube")
        super().__init__(color, *cube_sides, filled=filled)

    def get_volume(self):
        return round(pow(self.get_sides()[0], 3))



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())


# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

triang = Triangle((45, 67), 45, 45, 45)
triang.set_sides(10 ,10 ,10)
print(triang.get_sides())
print(triang.get_square())
print( len(triang))

