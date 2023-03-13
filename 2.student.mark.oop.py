class Object:
    def __init__(self):
        self.__name = []
        self.__id = []
    def setName(self, name):
        self.__name.append(name)
    def setId(self, id):
        self.__id.append(id)
    def getName(self, i):
        return self.__name[i]
    def getInfo(self, i):
        print("Id: ", self.__id[i]) 
        print("Name: ", self.__name[i])
class Student(Object):
    def __init__(self):
        super().__init__() #from Object
        self.__dob = []
    def setDob(self, dob):
        self.__dob.append(dob)
    def getInfo(self, i):
        super().getInfo(i) #from Object
        print("DoB:", self.__dob[i])
class Course(Object):
    def __init__(self):
        super().__init__() #from Object
        self.__marks = []
    def setMark(self, m):
        self.__marks.append(m)
    def getMark(self, i):
        print("Mark: ", self.__marks[i])

#create students list
Stu_list = Student()
nos = int(input("Input number of students: "))
for i in range(nos):
    Stu_list.setId(input("Input student id: ")) #from Object
    Stu_list.setName(input("Input student name: ")) #from Object
    Stu_list.setDob(input("Input student date of birth: ")) #from Student

#create course list
Cou_list = Course()
noc = int(input("Input number of courses: "))
for i in range(noc):
    Cou_list.setId(input("Input course id: ")) #from Object
    Cou_list.setName(input("Input course name: ")) #from Object
    for j in range(nos):
        Cou_list.setMark(float(input("Input course mark of student " + str(Stu_list.getName(j)) + ": ")))
   
#display information
for i in range(noc):
    print("- Course", i + 1)
    Cou_list.getInfo(i) #from Object
    for j in range(nos):
        print(" + Student", j + 1)
        Stu_list.getInfo(j) #from Student
        Cou_list.getMark(j + nos * i) #from Course

        