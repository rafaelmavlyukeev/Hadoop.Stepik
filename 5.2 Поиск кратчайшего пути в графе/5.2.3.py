# put your python code here
import sys
import itertools

inFile = open('input.txt')
lineCount = 1

V = set()  # множество вершин
E = set()  # множество ребер
W = dict()  # веса ребер
s = int()  # вершина старта
U = set()  # множетсво посещенных вершин
RU = set()  # множетсво непосещенных вершин
d = dict()  # длины кратчайшего пути

for line in inFile:
    if lineCount == 1:
        (verNum, edgeNum) = line.strip().split()
        lineCount += 1
    elif len(line.strip().split()) == 3:
        (v1, v2, w) = line.strip().split()
        W[(v1, v2)] = float(w)
        E.add((v1, v2))
        d[v1] = float('+inf')
        d[v2] = float('+inf')
        V.add(v1)
        V.add(v2)
    elif len(line.strip().split()) == 2:
        (s, f) = line.strip().split()
        d[s] = float(0)
        d[f] = float('+inf')
        V.add(s)
        V.add(f)

RU = V.copy()
RU.remove(s)
U.add(s)


def findNE(v, E):
    VN = set()
    for elem in E:
        if elem[0] == v:
            VN.add(elem)
    return list(VN)


def findNearest(v, E, W):
    NE = findNE(v, E)
    if len(NE) != 0:
        dist = float('+inf')
        for elem in NE:
            if W[elem] < dist:
                dist = W[elem]
                nv = elem[1]
        return (nv, dist)
    else:
        return (f, -1)


cv = s
lCv = s

while len(RU) != 0:
    lDist = d[cv]

    if findNearest(cv, E, W)[0] == lCv:
        d[cv] = -1
        break
    lCv = cv
    (cv, dist) = findNearest(cv, E, W)
    if dist == -1:
        d[cv] = -1
        break
    else:
        d[cv] = dist + lDist
    if cv == f:
        break
    RU.discard(cv)

for elem in d:
    if d[elem] == float('+inf'):
        d[elem] = -1

print(int(d[f]))
