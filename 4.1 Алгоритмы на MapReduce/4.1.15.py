# put your python code here
import sys

inFile = open('input.txt')

myList = list()
myDict = dict()
stripe = str()

for line in inFile:
    l = line.strip().split()
    for elem1 in l:
        myDict.clear()
        for elem2 in l:
            if elem1 != elem2:
                myDict[elem2] = myDict.get(elem2, 0) + 1

        myList.clear()
        for elem in list(myDict.items()):
            myList.append(elem[0] + ':' + str(elem[1]))
        print(elem1, ','.join(myList), sep='\t')
