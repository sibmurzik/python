# "Методы Юнит-тестирования"

import unittest
from runner_and_tournament import Tournament, Runner


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = list()

    def setUp(self):
        self.usein = Runner('Усэйн', speed=10)
        self.andrey = Runner('Андрей', speed=9)
        self.nik = Runner('Ник', speed=3)

    @classmethod
    def tearDownClass(cls):
        for item in cls.all_results:
            print(item)

    def test_start_usent_vs_nik(self):
        """
        Усэйн и Ник
        :return:
        """
        tournament = Tournament(90, self.usein, self.nik)
        self.all_results.append({key: str(value) for key, value in tournament.start().items()})
        maxKey = sorted(list(self.all_results[-1].keys()), reverse=True)[0]
        # print(maxKey)
        self.assertTrue(self.all_results[-1].get(maxKey) == 'Ник')

    def test_start_andrey_vs_nik(self):
        """
        Андрей и Ник
        :return:
        """
        tournament = Tournament(90, self.andrey, self.nik)
        self.all_results.append({key: str(value) for key, value in tournament.start().items()})
        maxKey = sorted(list(self.all_results[-1].keys()), reverse=True)[0]
        self.assertTrue(self.all_results[-1].get(maxKey) == 'Ник')

    def test_start_usein_vs_andrey_vs_nik(self):
        """
        Усэйн, Андрей и Ник.
        :return:
        """
        tournament = Tournament(90, self.usein, self.andrey, self.nik)
        self.all_results.append({key: str(value) for key, value in tournament.start().items()})
        maxKey = sorted(list(self.all_results[-1].keys()), reverse=True)[0]
        self.assertTrue(self.all_results[-1].get(maxKey) == 'Ник')

    def test_speed_comparasion(self):
        """
        Check speed relation vs result
        :return:
        """
        tournament = Tournament(90, self.usein, self.andrey, self.nik)
        speedDict = ({key: value.speed for key, value in tournament.start().items()})
        keys = sorted(list(speedDict.keys()))
        for i in range(len(keys) - 1):
            self.assertGreaterEqual(speedDict.get(keys[i]), speedDict.get(keys[i + 1]))


if __name__ == '__main__':
    unittest.main()
