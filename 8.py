#!/usr/bin/python3.5
# ITS LIT
import sys
import re
from collections import deque

# fuck it we're just making our own functions

width = 50 
height = 6
#row THEN col reference
m = [[0 for x in range(width)] for y in range(height)]

for command in sys.stdin:

    get = re.search(r'^rect (\d+)x(\d+)', command)
    if get:
        for i in range(int(get.group(2))): # row
            for j in range(int(get.group(1))): #col
                m[i][j] = 1

    get = re.search(r'^rotate row y=(\d+) by (\d+)', command)
    if get:
        row = int(get.group(1))
        rot = int(get.group(2))
        temp = [0]*width
        for j in range(width):
            temp[j] = m[row][j]
        for j in range(width):
            m[row][(j+rot)%width] = temp[j]

    get = re.search(r'^rotate column x=(\d+) by (\d+)', command)
    if get:
        col = int(get.group(1))
        rot = int(get.group(2))
        temp = [0]*height
        for i in range(height):
            temp[i] = m[i][col]
        for i in range(height):
            m[(i+rot)%height][col] = temp[i]

answer = 0
for i in range(height):
    for j in range(width):
        answer += m[i][j]
        if m[i][j] == 1:
            sys.stdout.write('*')
        else:
            sys.stdout.write(' ')
    sys.stdout.write('\n')
print(answer)

