import random

class Square_Matix_API:
    def __init__(self, size: int, martix = []):
        try:
            self.count = int(size)
        except ValueError:
            print("Matrix size must be integer")

        if isinstance(martix, list):
            self.matrix = martix
        else:
            self.matrix = []
            print("Not correct format of matrix , empty matrix created by default")

    def generate_random_numbers(self):
        numbers = [str(random.randint(0, 9)) for _ in range(self.count)]
        return ' '.join(numbers)

    def gen_new_matrix(self):
        self.matrix = []
        for i in range(self.count):
            martix_row = self.generate_random_numbers().split()
            matrix_number = [int(i) for i in martix_row]
            self.matrix.append(matrix_number)
        return self.matrix

    def print_matrix(self):
        print("Current Matrix")
        for row in self.matrix:
            print(row)

    def count_diagonal(self):
        result = 0
        for i in range(self.count):
            result += self.matrix[i][i]
        return result


sqr_matrix = Square_Matix_API(6, 'fff')
sqr_matrix.print_matrix()
sqr_matrix.gen_new_matrix()
sqr_matrix.print_matrix()
print(sqr_matrix.count_diagonal())












