import shutil
import os
from os import path

def main():
    mainDirectory = "/home/b1jeong/hpwren.ucsd.edu/HWB/HPWREN-FIgLib"
    for directory in os.listdir(mainDirectory):
        print(directory)
        if(os.path.isdir(mainDirectory + "/" + directory)):
            print("aye")
            indivudalFire(mainDirectory + "/" + directory)

    try:
        os.mkdir(mainDirectory+"/"+"AFTER")
    except FileExistsError:
        print("fin")
    try:
        os.mkdir(mainDirectory + "/" + "BEFORE")
    except FileExistsError:
        print("fin")

    oneMoreTime()



def convert(list):
    res = ''
    for i in list: 
        res += i     
    return res

def indivudalFire(currentDirectory):
    if currentDirectory.endswith("/"):
        currentDirectory = currentDirectory[:-1]
        print(currentDirectory)

    name = convert(convert(currentDirectory.split("-")[1:]).split("FIgLib/"))

    afterDir = currentDirectory + "/"+ name + "AFTER"
    beforeDir = currentDirectory +"/"+ name + "BEFORE"

    try:
        os.mkdir(afterDir)
    except FileExistsError:
        print("already run")
    try:
        os.mkdir(beforeDir)
    except FileExistsError:
        print("already run")

    for filename in os.listdir(currentDirectory):
        abspath = currentDirectory+"/"+filename
        if ord(filename[0]) <= 57 and filename.endswith(".jpg"):
            if("+" in filename):
                shutil.copy(abspath, afterDir)
            elif("-" in filename):
                shutil.copy(abspath, beforeDir)

def oneMoreTime():
    mainDirectory = "/home/b1jeong/hpwren.ucsd.edu/HWB/HPWREN-FIgLib"   
    for directory in os.listdir(mainDirectory):
        if(os.path.isdir(mainDirectory + "/" + directory)):
            for innerDir in os.listdir(mainDirectory):
                print(mainDirectory +"/" + "AFTER")
                # print(innerDir)
                name = convert(convert((mainDirectory+"/"+directory+innerDir).split("-")[1:]).split("FIgLib/"))
                if name.endswith("AFTER"):
                    shutil.move(mainDirectory + "/" + directory + "/"+ name, 
                        mainDirectory+"/"+"AFTER")

                elif innerDir.endswith("BEFORE"):
                    shutil.move(mainDirectory + "/" + directory + "/"+ name, 
                        mainDirectory+"/"+"BEFORE")

oneMoreTime()