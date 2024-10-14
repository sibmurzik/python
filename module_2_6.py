#Дополнительное практическое задание по модулю "Основные операторы"

seed_number = int(input("Введите число из первой вставки от 3 до 20: "))
result =""
if seed_number < 3 or seed_number > 20:
    print("Введено неправильное число")
else:
    for i in range(1, seed_number):
        for j in range(i, seed_number):
            if i == j :
                continue
            if seed_number % (i+j) == 0:
                result = result + str(i) + str (j)

#sample = 13141911923282183731746416515614713812911
#if (result == str(sampe)):
#    print("OK")

print("Нужный пароль: ",result)