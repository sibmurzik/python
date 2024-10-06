#"Базовые структуры данных"

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

student_arranged = sorted(tuple(students))
print(student_arranged)
average_grades = []
for g in grades:
    average_grades.append((sum(g)/ len(g)))

print(average_grades)


students_dict = dict(zip(student_arranged,average_grades))

print(students_dict)

