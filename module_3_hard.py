#Дополнительное практическое задание по модулю: "Подробнее о функциях."


def calculate_structure_sum(*args):
    counter = 0
    for i in args:
        if isinstance(i, (tuple, set, frozenset, list)):
            #print(i)
            counter += calculate_structure_sum(*i)
        elif isinstance(i, dict):
            temp_list =[]
            for key, values in i.items():
                temp_list.append(key)
                temp_list.append(values)
            #print(temp_list)
            counter += calculate_structure_sum(*temp_list)
        else:
            if isinstance(i, (int, float)):
                #print(i)
                counter += i

            else:
                #print(i, "len", len(i))
                counter += len(str(i))

    return counter










data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)

print(result)