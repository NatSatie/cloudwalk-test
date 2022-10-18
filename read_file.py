import re
from collections import OrderedDict

start_regex = re.compile(r".*InitGame:.*")

kill_regex = re.compile(r".*Kill:.*:(.*).*killed(.*)by(.*)")

def match_regex(logfile):
    with open(logfile, "r", encoding="utf-8") as fp:
        for line in fp.readlines():
            if start_regex.match(line):
                print(line)
            if kill_regex.match(line):
                print(line)
    return