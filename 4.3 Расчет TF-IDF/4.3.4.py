# put your python code here
import sys

myDict = dict()
inFile = open('input.txt')

for line in inFile:
    (word, doc, q) = line.strip().split('\t')
    print(word, doc + ';' + q + ';' + '1', sep='\t')
