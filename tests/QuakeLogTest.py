from MeansOfDeathEnum import MeansOfDeathEnum
from QuakeLog import QuakeLog, generateKillByMeans # Import the code to be tested
import unittest # test framework

class TestQuakeLog(unittest.TestCase):
    def setUp(self):
        self.quakeLog = QuakeLog(0, [], {}, {}, generateKillByMeans())

    def test_addPlayer_isInPlayerList(self):
        self.quakeLog.addPlayer("player_1")
        self.assertEqual(self.quakeLog.playerList, ["player_1"])

    def test_addKillPlayerByWorld_isKillTotalRegistered(self):
        self.quakeLog.addPlayer("player_1")
        self.quakeLog.addKillByWorld("player_1", MeansOfDeathEnum.MOD_FALLING)
        self.assertEqual(self.quakeLog.totalKills, 1)

    def test_addKillPlayerByWorld_isKillByMeansTotalRegistered(self):
        self.quakeLog.addPlayer("player_1")
        self.quakeLog.addKillByWorld("player_1", MeansOfDeathEnum.MOD_FALLING)
        self.assertEqual(self.quakeLog.killsByMeans["MOD_FALLING"], 1)

    def test_addKillPlayerByPlayer_isKillTotalRegistered(self):
        self.quakeLog.addPlayer("player_1")
        self.quakeLog.addPlayer("player_2")
        self.quakeLog.addKillByPlayer("player_1", "player_2", MeansOfDeathEnum.MOD_PLASMA)
        self.assertEqual(self.quakeLog.totalKills, 1)
    
    def test_addKillPlayerByPlayer_isKillByMeansTotalRegistered(self):
        self.quakeLog.addPlayer("player_1")
        self.quakeLog.addPlayer("player_2")
        self.quakeLog.addKillByPlayer("player_1", "player_2", "MeansOfDeathEnum.MOD_PLASMA")
        self.assertEqual(self.quakeLog.killsByMeans["MOD_PLASMA"], 1)

    def test_buildGameRegistered(self):
        playerList = ["player_1", "player_2"]
        killByPlayerList = {
            "player_1": 1,
            "player_2": 1
        }
        deathOfPlayersList = {
            "player_1": 1,
            "player_2": 1
        }
        killByMeans = self.buildDeathByMeans()
        killByMeans["MOD_TARGET_LASER"] = 2
        self.quakeLog = QuakeLog(2, playerList, killByPlayerList, deathOfPlayersList, killByMeans)
        self.assertEqual(self.quakeLog.buildGameReport(), {
            "players": ["player_1", "player_3"], # Error done on purpose to test the Github actions
            "total_kills": 2,
            "kills": {
                "player_1": 1,
                "player_2": 1
            },
            "deaths": {
                "player_1": 1,
                "player_2": 1
            },
            "kills_by_means": {
                "MOD_UNKNOWN": 0,
                "MOD_SHOTGUN": 0,
                "MOD_GAUNTLET": 0,
                "MOD_MACHINEGUN": 0,
                "MOD_GRENADE": 0,
                "MOD_GRENADE_SPLASH": 0,
                "MOD_ROCKET": 0,
                "MOD_ROCKET_SPLASH": 0,
                "MOD_PLASMA": 0,
                "MOD_PLASMA_SPLASH": 0,
                'MOD_RAILGUN': 0,
                "MOD_LIGHTNING": 0,
                "MOD_BFG": 0,
                "MOD_BFG_SPLASH": 0,
                "MOD_WATER": 0,
                "MOD_SLIME": 0,
                "MOD_LAVA": 0,
                "MOD_CRUSH": 0,
                "MOD_TELEFRAG": 0,
                "MOD_FALLING": 0,
                "MOD_SUICIDE": 0,
                "MOD_TARGET_LASER": 2,
                "MOD_TRIGGER_HURT": 0,
                "MOD_NAIL": 0,
                "MOD_CHAINGUN": 0,
                "MOD_PROXIMITY_MINE": 0,
                "MOD_KAMIKAZE": 0,
                "MOD_JUICED": 0,
                "MOD_GRAPPLE": 0
            }
        })

    def buildDeathByMeans(self):
        return {
            "MOD_UNKNOWN": 0,
            "MOD_SHOTGUN": 0,
            "MOD_GAUNTLET": 0,
            "MOD_MACHINEGUN": 0,
            "MOD_GRENADE": 0,
            "MOD_GRENADE_SPLASH": 0,
            "MOD_ROCKET": 0,
            "MOD_ROCKET_SPLASH": 0,
            "MOD_PLASMA": 0,
            "MOD_PLASMA_SPLASH": 0,
            'MOD_RAILGUN': 0,
            "MOD_LIGHTNING": 0,
            "MOD_BFG": 0,
            "MOD_BFG_SPLASH": 0,
            "MOD_WATER": 0,
            "MOD_SLIME": 0,
            "MOD_LAVA": 0,
            "MOD_CRUSH": 0,
            "MOD_TELEFRAG": 0,
            "MOD_FALLING": 0,
            "MOD_SUICIDE": 0,
            "MOD_TARGET_LASER": 0,
            "MOD_TRIGGER_HURT": 0,
            "MOD_NAIL": 0,
            "MOD_CHAINGUN": 0,
            "MOD_PROXIMITY_MINE": 0,
            "MOD_KAMIKAZE": 0,
            "MOD_JUICED": 0,
            "MOD_GRAPPLE": 0
        }

if __name__ == '__main__':
    unittest.main() # pragma: no cover
