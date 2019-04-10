# put your python code here
import sys

myDict = dict()
myDict2 = dict()
inFile = open('input.txt')

for line in inFile:
    (word, (doc, q, one)) = (line.strip().split('\t')[0], line.strip().split('\t')[1].split(';'))
    compWord = word + '#' + doc
    myDict[compWord] = q
    myDict2[word] = myDict2.get(word, 0) + 1

for elem in myDict:
    print(elem, myDict[elem], myDict2[elem.split('#')[0]], sep='\t')
