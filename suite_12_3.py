#"Систематизация и пропуск тестов".

import unittest
import runner_test, tourmament_test

runningST = unittest.TestSuite()
runningST.addTest(unittest.TestLoader().loadTestsFromTestCase(runner_test.RunnerTest))
runningST.addTest(unittest.TestLoader().loadTestsFromTestCase(tourmament_test.TournamentTest))
runner = unittest.TextTestRunner(verbosity= 2)
runner.run(runningST)