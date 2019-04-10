# put your python code here
import sys
import itertools

inFile = open('input.txt')
myList = list()

for line in inFile:
    l = line.strip().split()
    for elem1 in l:
        for elem2 in l:
            if elem1 != elem2:
                myList.append((elem1, elem2))

for elem in myList:
    print(elem[0] + ',' + elem[1], 1, sep='\t')
