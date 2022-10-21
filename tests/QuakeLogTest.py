from MeansOfDeathEnum import MeansOfDeathEnum
from QuakeLog import QuakeLog # Import the code to be tested
import unittest # test framework

class TestQuakeLog(unittest.TestCase):
    def test_addPlayer_isInPlayerList(self):
        quakeLog = QuakeLog(0)
        quakeLog.addPlayer("player_1")
        assert(quakeLog.playerList, ["player_1"])

    def test_addKillPlayerByWorld_isKillTotalRegistered(self):
        quakeLog = QuakeLog(0)
        quakeLog.addPlayer("player_1")
        quakeLog.addKillByWorld("player_1", MeansOfDeathEnum.MOD_FALLING)
        assert(quakeLog.totalKills, 1)

    def test_addKillPlayerByWorld_isKillByMeansTotalRegistered(self):
        quakeLog = QuakeLog(0)
        quakeLog.addPlayer("player_1")
        quakeLog.addKillByWorld("player_1", MeansOfDeathEnum.MOD_PLASMA)
        assert(quakeLog.killsByMeans[MeansOfDeathEnum.MOD_PLASMA], 1)

    def test_addKillPlayerByPlayer_isKillTotalRegistered(self):
        quakeLog = QuakeLog(0)
        quakeLog.addPlayer("player_1")
        quakeLog.addPlayer("player_2")
        quakeLog.addKillByPlayer("player_1", "player_2", MeansOfDeathEnum.MOD_PLASMA)
        assert(quakeLog.totalKills, 1)
    
    def test_addKillPlayerByPlayer_isKillByMeansTotalRegistered(self):
        quakeLog = QuakeLog(0)
        quakeLog.addPlayer("player_1")
        quakeLog.addPlayer("player_2")
        quakeLog.addKillByPlayer("player_1", "player_2", MeansOfDeathEnum.MOD_PLASMA)
        assert(quakeLog.killsByMeans[MeansOfDeathEnum.MOD_PLASMA], 1)

    

if __name__ == '__main__':
    unittest.main()
