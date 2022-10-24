from MeansOfDeathEnum import MeansOfDeathEnum
from QuakeLog import QuakeLog # Import the code to be tested
import unittest # test framework

class TestQuakeLog(unittest.TestCase):
    def setUp(self):
        self.quakeLog = QuakeLog()

    def test_addPlayer_isInPlayerList(self):
        self.quakeLog.addPlayer("player_1")
        assert(self.quakeLog.playerList, ["player_1"])

    def test_addKillPlayerByWorld_isKillTotalRegistered(self):
        self.quakeLog.addPlayer("player_1")
        self.quakeLog.addKillByWorld("player_1", MeansOfDeathEnum.MOD_FALLING)
        self.assertEquals(self.quakeLog.totalKills, 1)

    def test_addKillPlayerByWorld_isKillByMeansTotalRegistered(self):
        self.quakeLog.addPlayer("player_1")
        self.quakeLog.addKillByWorld("player_1", MeansOfDeathEnum.MOD_FALLING)
        self.assertEquals(self.quakeLog.killsByMeans["MOD_FALLING"], 1)

    def test_addKillPlayerByPlayer_isKillTotalRegistered(self):
        self.quakeLog.addPlayer("player_1")
        self.quakeLog.addPlayer("player_2")
        self.quakeLog.addKillByPlayer("player_1", "player_2", MeansOfDeathEnum.MOD_PLASMA)
        self.assertEquals(self.quakeLog.totalKills, 1)
    
    def test_addKillPlayerByPlayer_isKillByMeansTotalRegistered(self):
        self.quakeLog.addPlayer("player_1")
        self.quakeLog.addPlayer("player_2")
        self.quakeLog.addKillByPlayer("player_1", "player_2", "MeansOfDeathEnum.MOD_PLASMA")
        self.assertEquals(self.quakeLog.killsByMeans["MOD_PLASMA"], 1)

if __name__ == '__main__':
    unittest.main()
