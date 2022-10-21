from MeansOfDeathEnum import MeansOfDeathEnum


class QuakeLog:
  def __init__(self, gameIndex: int, totalKills: int = 0, playerList = [], killsByPlayersList = {}):
    self.gameIndex = gameIndex
    self.totalKills = totalKills
    self.playerList = playerList
    self.killsByPlayersList = killsByPlayersList
    self.killsByMeans = self.generateMeansOfDeathEnumList()

  def addPlayer(self, playerName : str):
    if (playerName != '<world>'):
      self.playerList.append(playerName)
      self.killsByPlayersList[playerName] = 0

  def addKillByPlayer(self, playerName: str, meansOfDeath: MeansOfDeathEnum):
    self.totalKills += 1
    self.killsByPlayersList[playerName] += 1
    self.killsByMeans[meansOfDeath] += 1

  def addKillByWorld(self, meansOfDeath: MeansOfDeathEnum):
    self.totalKills += 1
    self.killsByMeans[meansOfDeath] += 1

  def toString(self):
    gameResult = {}
    gameResult['total_kills'] = self.totalKills
    gameResult['players'] = self.playerList
    gameResult['kills'] = self.killsByPlayersList
    return gameResult

  def generateMeansOfDeathEnumList(self):
    killsByMeans = {}
    for i in MeansOfDeathEnum:
      killsByMeans[i] = 0
    return killsByMeans