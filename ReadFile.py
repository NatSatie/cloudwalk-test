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

# List of Quake games that have been read in log file.
quakeGameLogList = []

quakeLogList = {}

def matchRegex(logfile: str):
		with open(logfile, "r", encoding="utf-8") as fp:
			gameIndex = -1
			for line in fp.readlines():
				if startRegex.match(line):
					gameIndex += 1
					quakeGameLogList.append(QuakeLog(gameIndex))
				if killRegex.match(line):
					readKillLine(line, gameIndex)
				if shutdownRegex.match(line):
					gameName = "game_" + str(gameIndex)
					quakeLogList[gameName] = quakeGameLogList[gameIndex].toString()
		return json.dumps(quakeLogList, indent=2)

def readKillLine(line: str, gameIndex: int):
		lineMatched = killRegex.match(line)
		playerAlive = lineMatched.group(1).strip()
		playerDead = lineMatched.group(2).strip()
		meansOfDeath = MeansOfDeathEnum[lineMatched.group(3).strip()]
		isPlayerAddedToPlayerList(playerAlive, gameIndex)
		isPlayerAddedToPlayerList(playerDead, gameIndex)
		if (playerAlive != '<world>'):
			quakeGameLogList[gameIndex].addKillByPlayer(playerAlive, meansOfDeath)
		else:
			quakeGameLogList[gameIndex].addKillByWorld(meansOfDeath)

def isPlayerAddedToPlayerList(playerName: str, gameIndex: int):
	if playerName not in quakeGameLogList[gameIndex].playerList:
		quakeGameLogList[gameIndex].addPlayer(playerName)
