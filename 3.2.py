#!/usr/bin/python3.5

import sys
triangles = 0
linNum = 1
num = [[] for _ in range(5)]

for line in sys.stdin:
    num[linNum%3] = line.split()
    
    if linNum%3 == 0:
        for col in range(0,3):
            isTri = 1
            for a in range(0,3):
                if int(num[a][col]) + int(num[(a+1)%3][col]) <= int(num[(a+2)%3][col]):
                    isTri = 0
            triangles += isTri
    linNum+=1

print(triangles)

