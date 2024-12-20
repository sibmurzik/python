# "Блокировки и обработка ошибок"

import threading
from time import sleep
from random import randint



class Bank:
    lock = threading.Lock()

    def __init__(self, ):
        self.balance = 0

    def deposit(self):
        for i in range(100):
            addition = randint(50, 500)
            if self.balance + addition < 500 and not self.lock.locked():
                with self.lock:
                    self.balance += addition
                    print(f'Пополнение: {addition}. Баланс: {self.balance} \n')
            sleep(0.001)

    def take(self):
        for i in range(100):
            detuction = randint(50, 500)
            print(f'Запрос на {detuction}')
            if self.balance < detuction:
                print("Запрос отклонён, недостаточно средств \n")
            else:
                with self.lock:
                    self.balance -= detuction
                    print(f'Снятие: {detuction}. Баланс: {self.balance}\n')
            sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')



