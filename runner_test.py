# "Простые Юнит-Тесты"

import unittest
from runner import Runner

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        men = Runner('Ralf')
        for i in range(10):
            men.walk()
        self.assertEqual(men.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        men = Runner('Ralf')
        for i in range(10):
            men.run()
        self.assertEqual(men.distance, 100)

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

