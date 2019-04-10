# put your python code here
import sys

inFile = open('input.txt')


for line in inFile:
    l = line.strip().split()
    if l[1] == 'user10':
        print(line, end='')
