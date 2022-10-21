from QuakeLog import QuakeLog # Import the code to be tested
import unittest # test framework

class Test_TestQuakeLog(unittest.TestCase):
    def testValidatorAddPlayer(self):
        quakeLog = QuakeLog(0)
        quakeLog.addPlayer("Natalia")
        assert(quakeLog.playerList, ["Natalia"])

if __name__ == '__main__':
    unittest.main()
