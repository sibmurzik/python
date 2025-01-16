# "Простые Юнит-Тесты"
import logging
import unittest
from rt_with_exceptions import Runner

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            men = Runner('Ralf', speed= -5)
            for i in range(10):
                men.walk()
            self.assertEqual(men.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as err:
            logging.warning("Неверная скорость для Runner" , exc_info= True)
            self.assertTrue(False)


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            men = Runner(10)
            for i in range(10):
                men.run()
            self.assertEqual(men.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as err:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)
            self.assertTrue(False)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        men1 = Runner('Ralf')
        men2 = Runner('Patric')
        for i in range(10):
            men1.run()
            men2.walk()
        self.assertNotEqual(men1.distance, men2.distance)


if __name__ == '__main__':
    unittest.main()

