# put your python code here
import sys

A = set()

for line in sys.stdin:
    A.add(line.split('\t')[0])

B = sorted(list(A))
print(*B, sep='\n')
