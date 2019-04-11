# put your python code here
import sys
import re
d = str()

inFile = open('input.txt')

for line in inFile:
    (n, d, chTemp) = line.strip().split('\t')

    print(n, d, chTemp, sep='\t')

    ch = re.findall('\w+', chTemp)

    if d == 'INF':
        d = 'INF'
    else:
       d = str(int(d) + 1)

    for elem in ch:

        print(elem, d, '{}', sep='\t')
