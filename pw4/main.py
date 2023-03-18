import math
import numpy as np
import curses
import domains
from domains.Major import Main
from input import input
from output import output

def MainFunc(stdscr):
    main = Main()
    input(main)
    output(main)
    main.mainFunction()
    
curses.wrapper(MainFunc)
curses.endwin()