#!/usr/bin/python3.5

import sys
slot = 0
dic = {}
for char in sys.stdin.read():
    if char == '\n':
        maxSlot = slot
        slot = 0
        continue
    if slot in dic:
        if char in dic[slot]:
            dic[slot][char] += 1
        else:
            dic[slot][char] = 1
    else:
        dic[slot] = {}
        dic[slot][char] = 1
    slot += 1
print(dic)

answer = ''
for i in range(0,maxSlot):
    answer += sorted(dic[i].items(), key = lambda x: (-x[1], x[0]))[0][0]

print(answer)
