from multiprocessing import current_process
import re
from QuakeLog import QuakeLog
from MeansOfDeathEnum import MeansOfDeathEnum
import json

#   Example of init game
#   0:00 InitGame: \sv_floodProtect\1\sv_maxPing\0\sv_minPing\0\sv_maxRate\10000\sv_minRate\0\sv_hostname\Code Miner Server\g_gametype\0\sv_privateClients\2\sv_maxclients\16\sv_allowDownload\0\dmflags\0\fraglimit\20\timelimit\15\g_maxGameClients\0\capturelimit\8\version\ioq3 1.36 linux-x86_64 Apr 12 2009\protocol\68\mapname\q3dm17\gamename\baseq3\g_needpass\0
startRegex = re.compile(r".*InitGame:.*")

#   Example of kill, victim, killer and cause.
#       The killer might be a player or <world>.
#   1:08 Kill: 3 2 6: Isgalamido killed Mocinha by MOD_ROCKET
killRegex = re.compile(r".*Kill:.*:(.*).*killed(.*)by(.*)")

#   When the game is finished
shutdownRegex = re.compile(r".*ShutdownGame:")

#   Exemple of an item 
#   0:29 Item: 2 weapon_rocketlauncher
itemRegex = re.compile(r".*Item:")

class ReadFile:
	def __init__(self, logfile: str, reportList = {}, quakeGameLogList = [], gameIndex = -1, isReadingGame = False, currentGame = QuakeLog):
		self.logfile = logfile
		# List of Quake games that have been read in log file.
		self.reportList = reportList
		self.quakeGameLogList = quakeGameLogList
		self.gameIndex = gameIndex
		self.isReadingGame = isReadingGame
		self.currentGame = currentGame

	def getGameResults(self):
		with open(self.logfile, "r", encoding="utf-8") as fp:
			for line in fp.readlines():
				if startRegex.match(line):
					self.readStartLine()
				if killRegex.match(line):
					self.readKillLine(line)
				if shutdownRegex.match(line):
					self.readShutdownLine()
			else:
				if (self.isReadingGame):
					raise Exception("The game log doesn't have a Shutdown Game line. "
													+ "Make sure you have complete file.")
		return json.dumps(self.reportList, indent=2)

	def readShutdownLine(self):
		gameName = "game_" + str(self.gameIndex)
		self.reportList[gameName] = self.currentGame.toString()
		self.isReadingGame = False
		self.quakeGameLogList.append(self.currentGame)

	def readStartLine(self):
		# In case a game has ended but not properly shutted down
		if (self.isReadingGame):
			self.quakeGameLogList.append(self.currentGame)
			gameName = "game_" + str(self.gameIndex)
			self.reportList[gameName] = self.currentGame.toString()
		self.gameIndex += 1
		self.currentGame = QuakeLog(0, [], {}, {})
		self.isReadingGame = True

	def readKillLine(self, line: str):
		lineMatched = killRegex.match(line)
		playerAlive = lineMatched.group(1).strip()
		playerDead = lineMatched.group(2).strip()
		meansOfDeath = MeansOfDeathEnum[lineMatched.group(3).strip()]
		self.currentGame.isPlayerAddedToPlayerList(playerAlive)
		self.currentGame.isPlayerAddedToPlayerList(playerDead)
		if (playerAlive != '<world>'):
			self.currentGame.addKillByPlayer(playerAlive, playerDead, meansOfDeath)
		else:
			self.currentGame.addKillByWorld(playerDead, meansOfDeath)
