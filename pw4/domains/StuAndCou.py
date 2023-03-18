import math
import numpy as np
import curses

class Object:
    def __init__(self):
        self.screen = curses.initscr()
        self.__name = []
        self.__id = []
    def setName(self, name):
        self.__name.append(name)
    def setId(self, id):
        self.__id.append(id)
    def getName(self, i):
        return self.__name[i]
    def getInfo(self, i):
        self.screen.addstr(2, 0, "Id: " + self.__id[i]) 
        self.screen.addstr(3, 0, "Name: " + self.__name[i])
    def swapName(self, i, j):
        temp = self.__name[i]
        self.__name[i] = self.__name[j]
        self.__name[j] = temp
    def swapId(self, i, j):
        temp = self.__name[i]
        self.__id[i] = self.__id[j]
        self.__id[j] = temp
        
class Student(Object):
    def __init__(self):
        super().__init__() #from Object
        self.screen = curses.initscr()
        self.__dob = []
    def setDob(self, dob):
        self.__dob.append(dob)
    def getInfo(self, i):
        super().getInfo(i) #from Object
        self.screen.addstr(4, 0, "DoB:" + self.__dob[i])
    def swapInfo(self, i, j):
        super().swapId(i, j)
        super().swapName(i, j)
        temp = self.__dob[i]
        self.__dob[i] = self.__dob[j]
        self.__dob[j] = temp
        
class Course(Object):
    def __init__(self):
        super().__init__() #from Object
        self.screen = curses.initscr()
        self.__marks = []
        self.__credits = []
    def setMark(self, m):
        self.__marks.append(math.floor(m))
    def getMark(self, i):
        return self.__marks[i]
    def setCredit(self, c):
        self.__credits = np.array(c)
    def getCredit(self, i):
        return self.__credits[i]