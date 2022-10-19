import argparse
from ReadFile import matchRegex
import sys

if __name__ == "__main__":
	parser = argparse.ArgumentParser(
		description='Parse log file of quake game matches')
	parser.add_argument('-f', '--logfile',
						dest='logfile',
						metavar='logfile',
						action='store',
						help='TODO: add help description',
						required=True)

	args = parser.parse_args()
	print(args)
	if args:
		gameMatches = matchRegex(args.logfile)
		originalStdout = sys.stdout
		with open('gameListOutcome.txt', 'w') as f:
			sys.stdout = f
			print(gameMatches)
			sys.stdout = originalStdout