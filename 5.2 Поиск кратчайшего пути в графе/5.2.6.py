# put your python code here
import sys
import re

d = str()
dTemp = float()
dMin = float('+inf')
ch = set()
chStr = str()
lineCount = 1
nPrev = 0
dStr = str()

inFile = open('input.txt')

for line in inFile:

    (n, dTemp, chTemp) = (line.strip().split('\t')[0], float(line.strip().split('\t')[1]), line.strip().split('\t')[2])

    if lineCount != 1:
        if n == nPrev:
            if dTemp < dMin: dMin = dTemp
            ch.update(map(int, re.findall('\w+', chTemp)))
            chStr = ','.join(map(str, sorted(list(ch))))

            if dMin == float('+inf'):
                dStr = 'INF'
            else:
                dStr = int(dMin)

        elif n != nPrev:

            if dMin == float('+inf'):
                dStr = 'INF'
            else:
                dStr = int(dMin)

            chStr = ','.join(map(str, sorted(list(ch))))

            print(nPrev, dStr, '{' + chStr + '}', sep='\t')

            nPrev = n
            dMin = dTemp
            ch.clear()
    else:
        nPrev = n
        dMin = dTemp
        ch.update(map(int, re.findall('\w+', chTemp)))
        lineCount += 1

print(nPrev, dStr, '{' + chStr + '}', sep='\t')
