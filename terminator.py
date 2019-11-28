import curses
from curses import wrapper
import datetime


class Terminator:
    COLOR = {
        'RED': 1,
        'YELLOW': 2
    }

    def print(self, config, message: str, colorPair=0):
        self.stdscr.addstr(getTime())
        self.stdscr.addstr('[{}] {}\n'.format(config['prefix'], message),
                           curses.color_pair(colorPair))
        self.stdscr.getch()

    @staticmethod
    def colorInitializer():
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    def term(self, stdscr):
        self.stdscr = stdscr
        stdscr.clear()
        stdscr.addstr(getTime() + '\n')

    def __init__(self):
        self.stdscr = ''
        wrapper(self.term)
        self.colorInitializer()


def getTime():
    now = datetime.datetime.now()
    dtstring = '[{}.{}.{} - {}:{}:{}]'.format(now.year, now.month, now.day, now.hour, now.minute, now.second)
    return dtstring