#!/usr/bin/env python
from os import rename, listdir
import string

userInput = raw_input("Enter Command: ")

extensions = ['jpg', 'JPG', 'png', 'PNG']

list1 = []

fnames = listdir('.')
for fname in fnames:
    if fname[-3:] in extensions and fname[0] in string.digits:
        list1.append(fname[:-4])

for item in list1:
    print item

list1Sorted = sorted(list1, key=int)

for item in list1Sorted:
    print item

if userInput == "reorder":
    i = 1
    for item in list1Sorted:
        if item == str(i):
            i += 1
        else:
            for fname in fnames:
                if fname.startswith(list1Sorted[i - 1] + "."):
                    rename(fname, fname.replace(list1Sorted[i - 1] + ".", str(i) + "."))
            i += 1
elif userInput.startswith("insert "):
    userInputList = userInput.split(" ")
    i = int(userInputList[2])
    length = len(list1Sorted)
    x = 0
    while i <= length - x:
        for fname in fnames:
            if fname.startswith(str(length - x) + "."):
                rename(fname, fname.replace(str(length - x) + ".", str((length - x) + 1) + "."))
        x += 1
    for fname in fnames:
        if fname.startswith(userInputList[1] + "."):
            rename(fname, fname.replace(userInputList[1] + ".", userInputList[2] + "."))


# for fname in fnames:
#     if fname.startswith(badprefix*2):
#         rename(fname, fname.replace(badprefix, '', 1))