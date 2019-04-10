# put your python code here
import sys

inFile = open('input.txt')
myDict = dict()
lPrev = ''
iPrev = 0

for line in inFile:
    (i, l) = line.strip().split('\t')
    if (i, l) != (iPrev, lPrev):
        (iPrev, lPrev) = (i, l)
        myDict[l] = myDict.get(l, 0) + 1

for elem in myDict:
    print(elem, myDict[elem], sep='\t')
