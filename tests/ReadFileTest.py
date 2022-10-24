from ReadFile import ReadFile # Import the code to be tested
import unittest # test framework

class TestReadFile(unittest.TestCase):
    def setUp(self):
        self.readFile = ReadFile('input/game2.log')

    # TODO: add readShutdownLine test
    
    # TODO: add readStartLine test

    # TODO: add readKillLine test

    # TODO: add getGameResults test


if __name__ == '__main__':
    unittest.main() # pragma: no cover
