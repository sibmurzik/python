# "Декораторы"

def is_prime(func):
    def wrapper(n1, n2, n3):
        res = func(n1, n2, n3)
        for i in range (2, res // 2 +1):
            if res % i == 0:
                print("Составное")
                return res
        print("Простое")
        return res

    return wrapper


@is_prime
def sum_three(n1, n2, n3):
    return n1 + n2 + n3


result = sum_three(2, 3, 6)
print(result)

result = sum_three(1, 1, 98)
print(result)