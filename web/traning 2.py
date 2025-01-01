import random
import time
from threading import Thread
import queue


class Bulkas(Thread):
    def __init__(self, queqe: queue.Queue):
        self.queqe = queqe
        super().__init__()

    def run(self):
        while True:
            time.sleep(random.randint(1, 3))
            if random.random() > 0.9:
                self.queqe.put("Burn bulka")
            else:
                self.queqe.put("Good buolka")
            print("bulka", self.queqe.qsize())


class Cotletos(Thread):
    def __init__(self, queqe: queue.Queue, count):
        self.queqe = queqe
        self.count = count
        super().__init__()

    def run(self):

        while self.count:
            print(self.queqe.qsize())
            bulka = self.queqe.get()
            if bulka == "Good buolka":
                time.sleep(random.randint(1, 3))
                self.count -= 1
            print("Produced hamburgers", self.count)


queue = queue.Queue(maxsize=10)
t1 = Bulkas(queue)
t2 = Cotletos(queue, 20)

t1.start()
t2.start()

t1.join()
t2.join()
