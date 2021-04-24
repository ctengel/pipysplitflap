#!/usr/bin/env python3

"""Simulator of splitflap display using Curses"""


import time
import curses


class SplitFlap:
    """A splitflap display"""

    def __init__(self, win):
        self.win = win
        self.future =  ['                ',
                        '                ']
        self.current = ['                ',
                        '                ']

    def linestatus(self):
        """Check to see if lines are up to date or still updating"""
        overall = True
        individ = []
        for idx in range(len(self.current)):
            if self.future[idx] == self.current[idx]:
                individ.append(True)
            else:
                individ.append(False)
                overall = False
        return overall, individ

    def update(self, line=0, text=''):
        """Update display with a new string"""
        self.future[line] = '{:^16}'.format(text.upper())

    def steps(self):
        """Do single flap of all charachters"""
        for i in range(2):
            for j in range(16):
                if self.future[i][j] != self.current[i][j]:
                    newch = chr(ord(self.current[i][j]) + 1)
                    if newch == '`':
                        newch = ' '
                    tmp = list(self.current[i])
                    tmp[j] = newch
                    self.current[i] = ''.join(tmp)
                    self.win.addch(i+1, j+1, newch)

    def gountilfinished(self):
        """Step through flaps until display is accurate"""
        while not self.linestatus()[0]:
            self.steps()
            self.win.refresh()
            time.sleep(0.125)
        self.win.refresh()

    def addtotop(self, line):
        """Add a line of text to the top of the screen
        Moving down all lines beneath it one by one
        """
        for idx in reversed(range(len(self.future))):
            if self.future[idx].strip() and idx != len(self.future):
                self.future[idx + 1] = self.future[idx]
            self.gountilfinished()
        self.update(text=line)
        self.gountilfinished()


def initscr(stdscr):
    """Initiate screen and basic display"""
    stdscr.clear()
    curses.curs_set(False)
    assert curses.LINES > 3
    assert curses.COLS > 17
    win = curses.newwin(4, 18, 0, 0)
    win.box()
    return win

def main(stdscr):
    """Main curses function"""
    win = initscr(stdscr)
    mysf = SplitFlap(win)
    mysf.update(text='hello world')
    mysf.gountilfinished()
    win.getkey()
    mysf.addtotop('goodbye world')
    win.getkey()


if __name__ == "__main__":
    curses.wrapper(main)


#stdscr = curses.initscr()
#curses.noecho()
#curses.cbreak()
#stdscr.keypad(True)

#curses.nocbreak()
#stdscr.keypad(False)
#curses.echo()
#curses.endwin()
