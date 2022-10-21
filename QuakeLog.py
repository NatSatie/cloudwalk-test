from MeansOfDeathEnum import MeansOfDeathEnum


class QuakeLog:
  def __init__(self, totalKills: int = 0, playerList = [], killsByPlayersList = {}, deathOfPlayersList = {}):
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
    self.killsByMeans[str(meansOfDeath).split(".")[1]] += 1

  def addKillByWorld(self, playerNameVictim: str, meansOfDeath: MeansOfDeathEnum):
    self.totalKills += 1
    self.deathOfPlayersList[playerNameVictim] += 1
    self.killsByMeans[str(meansOfDeath).split(".")[1]] += 1

  def toString(self):
    gameResult = {}
    gameResult['total_kills'] = self.totalKills
    gameResult['players'] = self.playerList
    gameResult['kills'] = self.killsByPlayersList
    gameResult['deaths'] = self.deathOfPlayersList
    gameResult['kills_by_means'] = self.killsByMeans
    return gameResult

  def isPlayerAddedToPlayerList(self, playerName: str):
    if playerName not in self.playerList:
      self.addPlayer(playerName)

  def generateMeansOfDeathEnumList(self):
    killsByMeans = {}
    for meansOfDeath in MeansOfDeathEnum:
      killsByMeans[str(meansOfDeath).split(".")[1]] = 0
    return killsByMeans