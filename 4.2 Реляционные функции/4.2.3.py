# put your python code here
import sys

inFile = open('input.txt')

for line in inFile:
    print(line.strip().split()[2])
