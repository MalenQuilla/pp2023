#the compress by lzma module is working but the decompress isn't. So that i have commented that method

import zlib, gzip, bz2, lzma, tarfile, zipfile
import glob
import shutil
import curses
import os
import pickle

def output(self):
    self.Output()
  
#all compress methods  
def Zlib():
    data = b''
    with open("students.dat", "wb") as f2:
        for i in glob.glob("*.txt"):
            with open(i, "rb") as f1:
                data += f1.read()
        comp_data = zlib.compress(data, zlib.Z_BEST_COMPRESSION)
        f2.write(comp_data)
    curses.initscr().clear()
    curses.initscr().addstr(0, 0,"Compress success")
    curses.initscr().getch()
def Gzip():
    with gzip.open("students.dat.gz", "wb") as f2:
        for i in glob.glob("*.txt"):
            with open(i, "rb") as f1:
                shutil.copyfileobj(f1, f2)
    curses.initscr().clear()
    curses.initscr().addstr(0, 0,"Compress success")
    curses.initscr().getch()
def Bz2():
    data = b''
    with bz2.open("students.dat.bz2", "wb") as f2:
        for i in glob.glob("*.txt"):
            with open(i, "rb") as f1:
                data += f1.read()
        f2.write(data)
    curses.initscr().clear()
    curses.initscr().addstr(0, 0,"Compress success")
    curses.initscr().getch()
# def Lzma():
#     comp_data = b''
#     with open("students.dat.xz", "wb") as f2:
#         for i in glob.glob("*.txt"):
#             with open(i, "r") as f1:
#                 for data in f1.read(1024):
#                     comp_data += lzma.LZMACompressor().compress(data.encode("ascii"))
#         f2.write(comp_data)
#         f2.write(lzma.LZMACompressor().flush())
def Tar():
    with tarfile.open("students.dat.tar", "w") as f:
        for file in glob.glob("*.txt"):
            f.add(file)  
    curses.initscr().clear()
    curses.initscr().addstr(0, 0,"Compress success")
    curses.initscr().getch()
def Zip():
    with zipfile.ZipFile("students.dat.zip", "w") as f:
        for file in glob.glob("*.txt"):
            f.write(file)  
    curses.initscr().clear()
    curses.initscr().addstr(0, 0,"Compress success")  
    curses.initscr().getch()   
def Pickle():
    obj = []
    with open("courses.txt", "r") as f1:
        obj.append(f1.read())
    with open("students.txt", "r") as f2:
        obj.append(f2.read())
    with open("marks.txt", "r") as f3:
        obj.append(f3.read())
    with open("students(pickle).dat", "wb") as pickleFile:
        pickle.dump(obj, pickleFile)  
    curses.initscr().clear()
    curses.initscr().addstr(0, 0,"Compress success")  
    curses.initscr().getch() 
         
 
#all extract method
def deCompPhase2(): #this function decompress "students.dat.txt" that return from deZlib, deGzip and deBz2 functions
    with open("students.dat.txt", "r") as file:
        with open("courses.txt", "w") as f1:
            f1.write(file.readline())
        with open("marks.txt", "w") as f2:
            f2.write(file.readline())
        with open("students.txt", "w") as f3:
            f3.write(file.readline())
    os.remove("students.dat.txt")
def deZlib():
    with open("students.dat", "rb") as f1, open("students.dat.txt", "wb") as f2:
        data = f1.read()
        decomp_data = zlib.decompress(data)
        f2.write(decomp_data)
    deCompPhase2()
    curses.initscr().addstr(0, 0,"Successfully decompress zlib file")
def deGzip():
    with gzip.open("students.dat.gz", "rb") as f1, open("students.dat.txt", "wb") as f2:
        data = f1.read()
        f2.write(data)
    deCompPhase2()
    curses.initscr().addstr(1, 0,"Successfully decompress gzip file")
def deBz2():
    with bz2.open("students.dat.bz2", "rb") as f1, open("students.dat.txt", "wb") as f2:
        data = f1.read()
        f2.write(data)
    deCompPhase2()
    curses.initscr().addstr(2, 0,"Successfully decompress bz2 file")
# def deLzma():
#         with lzma.open("students.dat.xz", "r") as f1, open("students.dat.txt", "wb") as f2:
#             data = f1.read().decode("utf-8").split()
#             f2.write(data)
def deTar():
    with tarfile.open("students.dat.tar", "r") as tf:
        tf.extractall() 
    curses.initscr().addstr(3, 0,"Successfully decompress tar file")
def deZip():
    with zipfile.ZipFile("students.dat.zip", "r") as zf:
        zf.extractall()   
    curses.initscr().addstr(4, 0,"Successfully decompress zip file")  
def dePickle():
    with open("students(pickle).dat", "rb") as f:
        obj = pickle.load(f)
    with open("courses.txt", "w") as f1:
        f1.write(obj[0])
    with open("students.txt", "w") as f2:
        f2.write(obj[1])
    with open("marks.txt", "w") as f3:
        f3.write(obj[2])
    curses.initscr().addstr(5, 0, "Successfully decompress pickled file")
        
    
        
#this function will try to run all the decompress methodss
def deCompEverything(): 
    screen = curses.initscr()
    screen.clear()
    try:
        deZlib()
    except IOError:
        screen.addstr(0, 0,"No zlib compressed files...")
    try:
        deGzip()
    except IOError:
        screen.addstr(1, 0,"No gzip compressed files...")
    try:
        deBz2()
    except IOError:
        screen.addstr(2, 0,"No bz2 compressed files...")
    try:
        deTar()
    except IOError:
        screen.addstr(3, 0,"No tar compressed files...")
    try:
        deZip()
    except IOError:
        screen.addstr(4, 0,"No zip compressed files...")
    try:
        dePickle()
    except IOError:
        screen.addstr(5, 0, "No pickled compressed files...")
            
def compFiles(self):
    screen = curses.initscr()
    screen.clear()
    methods = ["zlib", "gzip", "bz2", "tarfile", "zipfile", "pickle"]
    for i in range(6):
        screen.addstr(i, 0, str(i + 1) + ". " + methods[i])
    screen.addstr(6, 0, "Please select a method to compress: ")
    row, col = self.screen.getyx()
    method = int(self.screen.getstr(row, col).decode())
    match method:
        case 1:
            return Zlib()
        case 2:
            return Gzip()
        case 3: 
            return Bz2()
        case 4:
            return Tar()
        case 5:
            return Zip()
        case 6:
            return Pickle()