# put your python code here
import sys

inFile = open('input.txt')
myDict = dict()
l = list()

for line in inFile:
    (e, s) = line.strip().split('\t')
    l.clear()
    if myDict.get(e, 0) == 0:
        l.append(s)
        myDict[e] = l.copy()
    else:
        l = myDict[e]
        l.append(s)
        myDict[e] = l.copy()

for elem in myDict:
    if len(myDict[elem]) > 1:
        print(elem)
