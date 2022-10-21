from MeansOfDeathEnum import MeansOfDeathEnum


class QuakeLog:
  def __init__(self, gameIndex: int, totalKills: int = 0, playerList = [], killsByPlayersList = {}, deathOfPlayersList = {}):
    self.gameIndex = gameIndex
    self.totalKills = totalKills
    self.playerList = playerList
    self.killsByPlayersList = killsByPlayersList
    self.deathOfPlayersList = deathOfPlayersList
    self.killsByMeans = self.generateMeansOfDeathEnumList()

  def addPlayer(self, playerName : str):
    if (playerName != '<world>'):
      self.playerList.append(playerName)
      self.killsByPlayersList[playerName] = 0
      self.deathOfPlayersList[playerName] = 0

  def addKillByPlayer(self, playerNameKiller: str, playerNameVictim: str, meansOfDeath: MeansOfDeathEnum):
    self.totalKills += 1
    self.killsByPlayersList[playerNameKiller] += 1
    self.deathOfPlayersList[playerNameVictim] += 1
    self.killsByMeans[meansOfDeath] += 1

  def addKillByWorld(self, playerNameVictim: str, meansOfDeath: MeansOfDeathEnum):
    self.totalKills += 1
    self.deathOfPlayersList[playerNameVictim] += 1
    self.killsByMeans[meansOfDeath] += 1

  def toString(self):
    gameResult = {}
    gameResult['total_kills'] = self.totalKills
    gameResult['players'] = self.playerList
    gameResult['kills'] = self.killsByPlayersList
    gameResult['deaths'] = self.deathOfPlayersList
    return gameResult

  def generateMeansOfDeathEnumList(self):
    killsByMeans = {}
    for i in MeansOfDeathEnum:
      killsByMeans[i] = 0
    return killsByMeans