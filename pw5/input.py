def input(self):
    self.Input()

def studentsFile(main):
    f = open("students.txt", "w")
    for i in range(main.getNos()):
        f.write("*Student " + str(i + 1) + ": ")
        f.write(main.getStulist().getFullInfo(i) + " ")
    f.write("\n")
    f.close()
    
def coursesFile(main):
    f = open("courses.txt", "w")
    for i in range(main.getNoc()):
        f.write("*Course " + str(i + 1) + ": ")
        f.write(main.getCoulist().getFullInfo(i) + " ")
    f.write("\n")
    f.close()
    
def marksFile(main):
    nos = main.getNos()
    f = open("marks.txt", "w")
    for i in range(main.getNoc()):
        f.write("**Course " + str(i + 1) + ": ")
        for j in range(nos):
            f.write("*Student " + str(j + 1) + ": ")
            f.write(str(main.getCoulist().getMark(j + nos * i)) + " ")
    f.write("\n")
    f.close()