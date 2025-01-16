# "Логирование бегунов"

import  logging
import  unittest
import runner_test


runningST = unittest.TestSuite()
runningST.addTest(unittest.TestLoader().loadTestsFromTestCase(runner_test.RunnerTest))
runner = unittest.TextTestRunner(verbosity= 2)
logging.basicConfig(level= logging.INFO, filemode= 'w', filename= 'runner_tests.log', encoding= 'UTF-8',
                        format="%(asctime)s ! %(levelname)s ! %(message)s")
runner.run(runningST)

