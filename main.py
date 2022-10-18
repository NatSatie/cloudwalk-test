import argparse

from read_file import match_regex

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Parse log file of quake game matches')
    parser.add_argument('-f', '--logfile',
                        dest='logfile',
                        metavar='logfile',
                        action='store',
                        help='your logfile fullpath',
                        required=True)

    args = parser.parse_args()
    print(args)
    if args:
        game_matches = match_regex(args.logfile)