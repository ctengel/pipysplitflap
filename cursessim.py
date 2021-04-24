#!/usr/bin/env python3


"""Simulator of splitflap display using Curses"""


import time
import curses


future =  ['                ',
           '                ']
current = ['                ',
           '                ']


def linestatus():
    """Check to see if lines are up to date or still updating"""
    overall = True
    individ = []
    for idx in range(len(current)):
        if future[idx] == current[idx]:
            individ.append(True)
        else:
            individ.append(False)
            overall = False
    return overall, individ

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

def gountilfinished(win):
    """Step through flaps until display is accurate"""
    while not linestatus()[0]:
        steps(win)
        win.refresh()
        time.sleep(0.125)
    win.refresh()

def initscr(stdscr):
    """Initiate screen and basic display"""
    stdscr.clear()
    curses.curs_set(False)
    assert curses.LINES > 3
    assert curses.COLS > 17
    win = curses.newwin(4, 18, 0, 0)
    win.box()
    return win

def addtotop(line, win):
    """Add a line of text to the top of the screen
    Moving down all lines beneath it one by one
    """
    for idx in reversed(range(len(future))):
        if future[idx].strip() and idx != len(future):
            future[idx + 1] = future[idx]
            gountilfinished(win)
    update(text=line)
    gountilfinished(win)

def main(stdscr):
    """Main curses function"""
    win = initscr(stdscr)
    update(text='hello world')
    gountilfinished(win)
    win.getkey()
    addtotop('goodbye world', win)
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
