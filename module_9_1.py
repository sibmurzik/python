# "Введение в функциональное программирование"

def apply_all_func(int_list, *functions):
    def convert_checker(x):
        try:
            int(x)
        except ValueError:
            return False
        else:
            return True

    mod_list = list(map(int, filter(convert_checker, int_list)))
    print(list(mod_list))
    result = dict()
    for fun in functions:
        result[fun.__name__] = fun(mod_list)
    return result


print(apply_all_func([6, 20, 'g', 15, 9, '7', 'ff'], max, min))
print(apply_all_func([6, 20,'hh' ,15, 9, '66'], len, sum, sorted))
