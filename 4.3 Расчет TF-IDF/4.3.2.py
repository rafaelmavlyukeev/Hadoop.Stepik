# put your python code here
import sys
import re

inFile = open('input.txt')

for line in inFile:
    docNum = line[:line.find(':')]
    text = re.findall("[\w]+", line[line.find(':') + 1:].strip())
    for word in text:
        print(word + '#' + docNum, 1, sep='\t')
