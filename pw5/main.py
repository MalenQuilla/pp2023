import math
import numpy as np
import curses
import domains
from domains.Major import Main
import input as IN
import output as OUT

def MainFunc(stdscr):
    OUT.deCompEverything()
    main = Main()
    
    #input
    IN.input(main)
    IN.studentsFile(main)
    IN.coursesFile(main)
    IN.marksFile(main)
    
    #output
    OUT.output(main)
    OUT.compFiles(main)
    
    main.mainFunction()
     
curses.wrapper(MainFunc)
curses.endwin()