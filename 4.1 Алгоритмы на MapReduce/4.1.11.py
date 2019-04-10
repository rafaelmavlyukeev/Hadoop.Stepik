# put your python code here
# put your python code here
import sys

for line in sys.stdin:
    print(line.strip().split(',')[1], 1, sep='\t')
