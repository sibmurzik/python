import unittest
from runner import Runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        men = Runner('Ralf')
        for i in range(10):
            men.walk()
        self.assertEqual(men.distance, 50)



    def test_run(self):
        men = Runner('Ralf')
        for i in range(10):
            men.run()
        self.assertEqual(men.distance, 100)


    def test_challenge(self):
        men1 = Runner('Ralf')
        men2 = Runner('Patric')
        for i in range(10):
            men1.run()
            men2.walk()
        self.assertNotEqual(men1.distance, men2.distance)


if __name__ == '__main__':
    unittest.main()

