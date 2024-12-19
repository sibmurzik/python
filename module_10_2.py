# "Потоки на классах"
import threading
import time


class Knight(threading.Thread):
    enemies = 100

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'"{self.name}, на нас напали!".')
        days = 0
        remained_enimies = self.enemies
        while remained_enimies > 0:
            time.sleep(1)
            days += 1
            remained_enimies -= self.power
            print(f'{self.name} сражается {days} день(дня)..., осталось {remained_enimies} воинов."')
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
