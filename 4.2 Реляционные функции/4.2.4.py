# put your python code here
import sys

inFile = open('input.txt')
i = 0

for line in inFile:
    if i != line.split('\t')[0]:
        i = line.split('\t')[0]
        print(i)
       