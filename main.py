import argparse
import asyncio
from ReadFile import ReadFile
import sys

def argumentParser():
	parser = argparse.ArgumentParser(
		description='Parse log file of quake game matches')
	parser.add_argument('-i', '--input',
						dest='logfile',
						metavar='logfile',
						action='store',
						help='Read the file path of the Quake Game Log.',
						required=True)
	parser.add_argument('-o', '--output',
						dest='output',
						metavar='output',
						action='store',
						help='Write the output file path of the Quake Game Log.',
						required=True)
	return parser.parse_args()

def writeOutputFile(outputFile: str, gameResult):
	outputFile = args.output + ".json"
	originalStdout = sys.stdout
	with open(outputFile, 'w') as f:
		sys.stdout = f
		print(gameResult)
		sys.stdout = originalStdout

if __name__ == "__main__":
	args = argumentParser()
	if args:
		readFile = ReadFile(logfile=args.logfile)
		gameResult = readFile.getGameResults()
		writeOutputFile(outputFile=args.output, gameResult=gameResult)