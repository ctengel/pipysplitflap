#!/usr/bin/env python3

import time
import curses

future =  ['                ',
           '                ']
current = ['                ',
           '                ']


def update(line=0, text=''):
    future[line] = '{:^16}'.format(text.upper())

def steps(win):
    for i in range(2):
        for j in range(16):
            if future[i][j] != current[i][j]:
                newch = chr(ord(current[i][j]) + 1)
                if newch == '[':
                    newch == ' '
                tmp = list(current[i])
                tmp[j] = newch
                current[i] = ''.join(tmp)
                win.addch(i+1,j+1,newch)

def main(stdscr):
    stdscr.clear()
    curses.curs_set(False)
    assert curses.LINES > 3
    assert curses.COLS > 17
    win = curses.newwin(4, 18, 0, 0)
    win.box()
    #win.addstr(1, 1, 'hello world')
    #win.addch(2, 1, 'a')
    update(text='hello world')
    for i in range(256):
        steps(win)
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
