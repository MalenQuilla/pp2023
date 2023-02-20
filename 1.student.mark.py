def insert_stu():
    a = []
    x = input("Input student id: ")
    a.append(x)
    x = input("Input student name: ")
    a.append(x)
    x = input("Input student DoB: ")
    a.append(x)
    return a
def insert_course():
    a = []
    x = input("Input course id: ")
    a.append(x)
    x = input("Input course name: ")
    a.append(x)
    return a
def insert_marks(n, s):
    a = []
    for i in range(n):
        x = float(input("Input course mark of student " + s[i][1] + ": "))
        a.append(x)
    return a

n = int(input("Input number of student in class: "))
stu_list = []
for i in range(0, n):
    stu_list.append(insert_stu())

m = int(input("Input number of course: "))
course_list = []
for i in range(0, m):
    course_list.append(insert_course())

marks_list = []
for i in range(m):
    print("Course " + course_list[i][1] + ": ")
    marks_list.append(insert_marks(n, stu_list))
    
print("List of courses: ")
print(course_list)
print("List of students: ")
print(stu_list)
for i in range(m):
    print("Course " + course_list[i][1])
    for j in range(n):
        print(stu_list[j], ": ", str(marks_list[i][j]))