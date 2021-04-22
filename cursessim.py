#!/usr/bin/env python3

"""Simulator of splitflap display using Curses"""

import time
import curses

future =  ['                ',
           '                ']
current = ['                ',
           '                ']


def update(line=0, text=''):
    """Update display with a new string"""
    future[line] = '{:^16}'.format(text.upper())

def steps(win):
    """Do single flap of all charachters"""
    for i in range(2):
        for j in range(16):
            if future[i][j] != current[i][j]:
                newch = chr(ord(current[i][j]) + 1)
                if newch == '`':
                    newch = ' '
                tmp = list(current[i])
                tmp[j] = newch
                current[i] = ''.join(tmp)
                win.addch(i+1, j+1, newch)

def main(stdscr):
    """Main curses function"""
    stdscr.clear()
    curses.curs_set(False)
    assert curses.LINES > 3
    assert curses.COLS > 17
    win = curses.newwin(4, 18, 0, 0)
    win.box()
    update(text='hello world')
    for _ in range(64):
        steps(win)
        win.refresh()
        time.sleep(0.125)
    win.refresh()
    win.getkey()
    update(line=1, text='hello world')
    for _ in range(64):
        steps(win)
        win.refresh()
        time.sleep(0.125)
    update(line=0, text='goodbye world')
    for _ in range(64):
        steps(win)
        win.refresh()
        time.sleep(0.125)
    win.refresh()
    win.getkey()


curses.wrapper(main)


#stdscr = curses.initscr()
#curses.noecho()
#curses.cbreak()
#stdscr.keypad(True)

#curses.nocbreak()
#stdscr.keypad(False)
#curses.echo()
#curses.endwin()
