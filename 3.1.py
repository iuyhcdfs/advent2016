#!/usr/bin/python3.5

import sys
triangles = 0

for line in sys.stdin:
    num = line.split()
    isTri = 1
    for a in range(0,3):
        if int(num[a]) + int(num[(a+1)%3]) <= int(num[(a+2)%3]):
            isTri = 0
    triangles += isTri
print(triangles)

