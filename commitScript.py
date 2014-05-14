# Author: K-4U
# Written for Modjam 3
# This script will commit your files to the git repository every 15 minutes

repoDir = "/Path/To/Your/Working/Copy"
print_debug = True

# DO NOT CHANGE ANYTHING BELOW THIS LINE UNLESS YOU KNOW WHAT YOU ARE DOING!

import time
import os
import string
from subprocess import *

def command(x):
    if(print_debug):
        print(x)
    return str(Popen(x, stdout=PIPE, shell=True).communicate()[0])

def rm_empty(L): return [l for l in L if (l and l!="")]

def getUntracked():
    os.chdir(repoDir)
    status = command("git status")
    if "# Untracked files:" in status:
        untf = status.split("# Untracked files:")[1][1:].split("\n")
        return rm_empty([x[2:] for x in untf if string.strip(x) != "#" and x.startswith("#\t")])
    else:
        return []

def getNew():
    os.chdir(repoDir)
    status = command("git status").split("\n")
    return [x[14:] for x in status if x.startswith("#\tnew file:   ")]

def getModified():
    os.chdir(repoDir)
    status = command("git status").split("\n")
    return [x[14:] for x in status if x.startswith("#\tmodified:   ")]

def getDeleted():
    os.chdir(repoDir)
    status = command("git status").split("\n")
    return [x[14:] for x in status if x.startswith("#\tdeleted: ")]

def add(files):
    os.chdir(repoDir)
    if len(files) > 0:
        files2 = []
        for f in files:
            if f.find(' '):
                f = '"' + f + '"'
            files2.append(f)
        command("git add %s" % ('*'.join(files2).replace("*"," ")))

def remove(files):
    os.chdir(repoDir)
    if len(files) > 0:
        files2 = []
        for f in files:
            if f.find(' '):
                f = '"' + f + '"'
            files2.append(f)

        command("git rm %s" % ('*'.join(files2).replace("*"," ")))

def commit(logMessage):
    os.chdir(repoDir)
    command("git commit -m\"%s\"" % logMessage)

def push():
    os.chdir(repoDir)
    command("git push")


timeCount = 1
while 1:
    timeCount -= 1
    print("Committing to repository in %d minutes!"%timeCount)
    if(timeCount == 0):
        timeCount = 15
        #This should run about every 15 minutes..
        untracked = getUntracked()
        new = getNew()
        modified = getModified()
        deleted = getDeleted()
        if(print_debug):
            print("Untracked:")
            print( untracked )
            print("New:")
            print( new )
            print("Modified:")
            print( modified )
            print("Deleted:")
            print( deleted )


        add(untracked)
        add(modified)
        remove(deleted)

        if(len(deleted) > 0 or len(modified) > 0 or len(untracked) > 0):
            commit("commit from %s. %d deletions, %d adds, %d modifications" % (time.strftime("%c"), len(deleted), len(untracked), len(modified)))
            push()
    time.sleep(60)
