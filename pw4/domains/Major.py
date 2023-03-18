import math
import numpy as np
import curses
from domains.StuAndCou import Student
from domains.StuAndCou import Course

class Main:
    def __init__(self):
        self.screen = curses.initscr()
        self.__Stu_list = Student()
        self.__Cou_list = Course()
        self.__nos = 0
        self.__noc = 0
    def mainFunction(self):
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        self.screen.clear()
        self.screen.refresh()
        self.screen.getch()
    def GPACalculator(self, coulist, couNum, stuNum, stuIndex): #GPA calculator function
        i = 0
        sum = 0
        sum_cred = 0
        while i < couNum:
            sum += coulist.getMark(stuIndex + i * stuNum) * coulist.getCredit(i)
            sum_cred += coulist.getCredit(i)
            i += 1
        return sum / sum_cred
    def WAMCalculator(self, coulist, couNum, stuNum, stuIndex): #WAM calculator function
        i = 0
        sum = 0
        sum_cred = 0
        while i < couNum:
            if coulist.getMark(stuIndex + i * stuNum) >= 10:
                sum += coulist.getMark(stuIndex + i * stuNum) * coulist.getCredit(i)
                sum_cred += coulist.getCredit(i)
            i += 1
        if sum_cred != 0:
            return sum / sum_cred
        else: return 0
    def NumToLetPoint(self, point): #Function that convert number point to letter point
        match point:
            case 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9:
                return "F"
            case 10:
                return "D"
            case 11:
                return "C"
            case 12:
                return "C+"
            case 13:
                return "B"
            case 14 | 15:
                return "B+"
            case 16 | 17:
                return "A"
            case 18 | 19 | 20:
                return "A+"
            case _:
                return "Invalid GPA"
    def Sort(self, stulist, GPAs, numStu): #Sort Student list by GPA descending function
        if numStu == 1:
            self.screen.addstr(1, 0, "There is only one student!")
            return
        isSwap = True
        while isSwap == True:
            for i in range(numStu - 1):
                isSwap = False
                for j in range(numStu - i - 1):
                    if GPAs[j] < GPAs[j + 1]:
                        temp = GPAs[j]
                        GPAs[j] = GPAs[j + 1]
                        GPAs[j + 1] = temp
                        stulist.swapInfo(j, j + 1) #from Student
                        isSwap = True
                if isSwap == False:
                    for i in range(numStu):
                        self.screen.getch()
                        self.screen.move(1, 0)
                        self.screen.clrtobot()
                        self.screen.addstr(1, 0, "*Student " + str(i + 1) + ": ")
                        stulist.getInfo(i) #from Student
                        self.screen.addstr(5, 0, "GPA: " + str(self.NumToLetPoint(math.floor(GPAs[i]))))
                    return
                
    def Input(self): #Input information
        curses.curs_set(0)
        
        self.screen.keypad(True)
        curses.echo()  
    
        #create students list
        self.screen.addstr(0, 0, "Input number of students: ")
        row, col = self.screen.getyx()
        self.__nos = int(self.screen.getstr(row, col).decode())
        self.screen.clear()
        for i in range(self.__nos):
            self.screen.addstr(0, 0, "*Student " + str(i + 1) + ": ")
            self.screen.addstr(1, 0, "Input student id: ")
            row, col = self.screen.getyx()
            self.__Stu_list.setId(self.screen.getstr(row, col).decode())#from Object
            self.screen.addstr(2, 0, "Input student name: ")
            row, col = self.screen.getyx()
            self.__Stu_list.setName(self.screen.getstr(row, col).decode())#from Object
            self.screen.addstr(3, 0, "Input student date of birth: ")
            row, col = self.screen.getyx()
            self.__Stu_list.setDob(self.screen.getstr(row, col).decode())#from Student
            self.screen.clear()
            
        #create course list
        self.screen.addstr(0, 0, "Input number of courses: ")
        row, col = self.screen.getyx()
        self.__noc = int(self.screen.getstr(row, col).decode())
        self.screen.clear()
        credit = []
        for i in range(self.__noc):
            self.screen.addstr(0, 0, "*Course " + str(i + 1) + ": ")
            self.screen.addstr(1, 0, "Input course id: ")
            row, col = self.screen.getyx()
            self.__Cou_list.setId(self.screen.getstr(row, col).decode())#from Object
            self.screen.addstr(2, 0, "Input course name: ")
            row, col = self.screen.getyx()
            self.__Cou_list.setName(self.screen.getstr(row, col).decode())#from Object
            self.screen.addstr(3, 0, "Input number of unit credits in course: ")
            row, col = self.screen.getyx()
            credit.append(int(self.screen.getstr(row, col).decode()))
            for j in range(self.__nos):
                self.screen.addstr(j + 4, 0, "Input course mark of student " + str(self.__Stu_list.getName(j)) + ": ")
                row, col = self.screen.getyx()
                mark = float(self.screen.getstr(row, col).decode())
                while mark > 20 or mark < 0:
                    self.screen.move(j + 4, 0)
                    self.screen.clrtoeol()
                    self.screen.addstr(j + 4, 0, "Input course mark of student " + str(self.__Stu_list.getName(j)) + ": ")
                    row, col = self.screen.getyx()
                    mark = float(self.screen.getstr(row, col).decode())
                self.__Cou_list.setMark(mark) #from Course
            self.screen.clear()
        self.__Cou_list.setCredit(credit) #from Course
    
    def Output(self):
        #display information
        for i in range(self.__noc):
            self.screen.addstr(0, 0, "**Course" + str(i + 1))
            self.__Cou_list.getInfo(i) #from Object
            for j in range(self.__nos):
                self.screen.getch()
                self.screen.move(1, 0)
                self.screen.clrtobot()
                self.screen.addstr(1, 0, "*Student" + str(j + 1))
                self.__Stu_list.getInfo(j) #from Student
                self.screen.addstr(5, 0, "Mark " + str(self.__Cou_list.getMark(j + self.__nos * i))) #from Course
            self.screen.getch()
            self.screen.clear()
        GPAs = []
        for i in range(self.__nos):
            GPAs.append(self.GPACalculator(self.__Cou_list, self.__noc, self.__nos, i))
            self.screen.addstr(i * 3, 0, "**Course " + self.__Cou_list.getName(i) + ": ")
            self.screen.addstr(i * 3 + 1, 0, "GPA of student " + str(self.__Stu_list.getName(i)) + ": " + self.NumToLetPoint(math.floor(self.GPACalculator(self.__Cou_list, self.__noc, self.__nos, i))))
            self.screen.addstr(i * 3 + 2, 0, "WAM of student " + str(self.__Stu_list.getName(i)) + ": " + str(math.floor(self.WAMCalculator(self.__Cou_list, self.__noc, self.__nos, i))))
        self.screen.getch()
        self.screen.clear()
        
        #Sort and display new student list
        self.screen.addstr(0, 0, "**Student list after sorted: ")
        self.Sort(self.__Stu_list, GPAs, self.__nos)
        self.screen.getch()