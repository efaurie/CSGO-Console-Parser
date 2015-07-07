import argparse

from parser_fns import *
from LogTailer import LogTailer
from ScoreBoard import ScoreBoard
from ConsoleParserConfigReader import ConsoleParserConfigReader

def init_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-config', default='../resources/csgo-parser.conf', help='The path to the CSGO console.log output location.')
    return parser.parse_args()

def run(config):
    scoreboard = ScoreBoard()
    tailer = LogTailer(config.log_location)
    tailer.start()
    while True:
        current_line = tailer.poll()
        parse(current_line, scoreboard)


if __name__ == '__main__':
    args = init_parser()

    print '[+] Initializing CSGO Console Parser'
    config = ConsoleParserConfigReader(args.config)

    print '[+] Config Loaded: Starting Stream'
    run(config)
