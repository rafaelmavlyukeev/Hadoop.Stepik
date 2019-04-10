# put your python code here
import sys

myDict = dict()
inFile = open('input.txt')

for line in inFile:
    (wordComp, count) = line.strip().split('\t')
    myDict[wordComp] = myDict.get(wordComp, 0) + 1

for elem in myDict:
    (word, docNum) = elem.split('#')
    print(word, docNum, myDict[elem], sep='\t')
