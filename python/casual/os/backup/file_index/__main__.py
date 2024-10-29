import os
import shutil

#test1
"""
test1
os.makedirs("backup/new")
shutil.copytree("source", "backup/new/source")
"""

#test2
"""
def test2(workpath, totalsize = 0):
    checklist = os.listdir(workpath)

    for i in checklist:
        curpath = workpath + "/" + i
        if os.path.isdir(curpath):
            totalsize += test2(curpath)
        else:
            totalsize += os.path.getsize(curpath)
    
    return totalsize


oprate = "source"

size = 0
size = test2(oprate)
print(size)

# totalsize = 0
# totalsize = os.path.getsize(oprate)
# print(totalsize)
"""

#test3(不包含子目录)
"""
def test3ns(workpath):
    checklist = os.listdir(workpath)

    for i in checklist:
        curpath = workpath + "/" + i
        name = i.split(".")
        if "bmp" in name:
            os.remove(curpath)

oprate = "source"
test3ns(oprate)
"""

#test3(包含子目录)
"""
def test3s(workpath):
    checklist = os.listdir(workpath)

    for i in checklist:
        curpath = workpath + "/" + i
        if os.path.isdir(curpath):
            test3s(curpath)
        else:
            name = i.split(".")
            if "bmp" in name:
                os.remove(curpath)

oprate = "source"
test3s(oprate)
"""

#test4
def test5(workpath):
    checklist = os.listdir(workpath)

    for i in checklist:
        curpath = workpath + "/" + i
        name = i.split(".")
        if "avi" in name:
            newname = workpath + "/" + name[0] + ".dll"
            os.rename(curpath, newname)

oprate = "source"
test5(oprate)

#test5
"""
def test5(workpath):
    checklist = os.listdir(workpath)

    for i in checklist:
        curpath = workpath + "/" + i
        if os.path.isdir(curpath):
            test5(curpath)
        else:
            name = i.split(".")
            if "avi" in name:
                newname = workpath + "/" + name[0] + ".dll"
                os.rename(curpath, newname)

oprate = "source"
test5(oprate)
"""

