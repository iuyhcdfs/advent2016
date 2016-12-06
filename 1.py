#!/usr/bin/python3.5

import sys
from collections import deque
from operator import mul, add

string = sys.stdin.read()
array = string.split(", ")

compass = deque([1,0,0,0])
travel = deque([0,0,0,0])
first = 1
been = {}
x = 0
y = 0
for line in array:
    turn = line[0]
    dist = line[1:]
    if turn == "L":
        compass.rotate(-1)
    if turn == "R":
        compass.rotate(1)
    for i in range(0,4):
        for whateverrrr in range(0,int(dist)):
            if compass[i] == 0:
                break
            travel[i] += compass[i]
            x = travel[1] - travel[3]
            y = travel[0] - travel[2]
            if (str(x)+","+str(y)) in been and first == 1:
                print ("2nd visit to "+str(x)+" and "+str(y)) 
                print ("manhattan distance is "+str(abs(x)+abs(y)))
                first = 0
            been[str(x)+","+str(y)] = 1;

x = travel[1] - travel[3]
y = travel[0] - travel[2]
print ("last x = "+str(x))
print ("last y = "+str(y))
print ("manhattan = "+str(abs(x)+abs(y)))
