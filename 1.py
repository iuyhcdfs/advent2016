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
    for x in range(0,4):
        for y in range(1,(int(dist)+1))
            travel[x] += compass[x]
            x = travel[1] - travel[3]
            y = travel[0] - travel[2]
            been[str(x)+","+str(y)] = 1;
            if (str(x)+","+str(y)) in been and first == 1:
                print ("2nd visit to "+str(x)+" and "+str(y)) 
                print ("manhattan distance is "+str(x+y))
                first = 0
    

x = travel[1] - travel[3]
y = travel[0] - travel[2]
print ("last x = "+str(x))
print ("last y = "+str(y))
print ("manhattan = "+str(x+y))
