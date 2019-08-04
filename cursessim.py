#!/usr/bin/env python3

import time
import curses

future =  ['                ',
           '                ']
current = ['                ',
           '                ']


def update(line=0, text=''):
    future[line] = sprintf('%16s', text)

def steps(win):
    for i in range(2):
        for j in range(16):
            if future[i][j] != current[i][j]:
                current[i][j] = current[i][j] + 1
                win.addch(i+1,j+1,current[i][j]

def main(stdscr):
    stdscr.clear()
    curses.curs_set(False)
    assert curses.LINES > 3
    assert curses.COLS > 17
    win = curses.newwin(4, 18, 0, 0)
    win.box()
    win.addstr(1, 1, 'hello world')
    win.addch(2, 1, 'a')
    win.refresh()
    time.sleep(1)
    win.addch(2, 1, 'b')
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
