import sys
import itertools
C = list()

for line in sys.stdin:
    C.extend(itertools.product(line.split()[0], line.split()[1].split(',')))

for comb in C:
    print(comb[0] + ',' + comb[1], 1, sep='\t')
