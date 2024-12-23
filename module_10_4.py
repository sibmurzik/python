# "Очереди для обмена данными между потоками."
import threading
from random import randint
import time
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        # print("new guest: ", name)

    def run(self):
        time.sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables: Table):
        self.queue = Queue()
        self.tables = [table for table in tables]
        # print(list(table.number for table in tables))

    def guest_arrival(self, *guests):
        for guest in guests:
            free_table = self.get_free_tables()
            if len(free_table) > 0:
                free_table[0].guest = guest
                guest.start()
                print(guest.name, "сел(-а) за стол номер", free_table[0].number)
            else:
                self.queue.put(guest)
                print(guest.name, " в очереди")

    def discuss_guests(self):
        while len(self.get_free_tables()) < len(self.tables) or not self.queue.empty():
            for table in tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(table.guest.name, " покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None
                    if not self.queue.empty():
                        table.guest = self.queue.get()
                        print(table.guest.name, "вышел(-ла) из очереди и сел(-а) за стол номер", table.number)
                        table.guest.start()

        #for table in self.get_free_tables():
        #    print(table.number," ", table.guest)

    def get_free_tables(self):
        return list([table for table in tables if table.guest is None])


# Создание столов

tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()
