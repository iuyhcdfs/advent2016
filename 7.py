#!/usr/bin/python3.5

import sys

numValid = 0
# youre just comparing last 4 chars. way simpler than dictionary index
for line in sys.stdin:
    hasABBA = 0
    badABBA = 0
    inBracket = 0
    for i in range(3, len(line)):
        if inBracket == 0 and line[i] == '[':
            inBracket = 1
            continue 
        if inBracket == 1 and line[i] == ']':
            inBracket = 0
            continue
        if line[i] == line[i-3] and line[i-1] == line[i-2] and line[i] != line[i-1]:
            if inBracket == 1:
                badABBA = 1
            if inBracket == 0:
                hasABBA = 1

    if hasABBA == 1 and badABBA == 0:
        numValid += 1

print(numValid)
