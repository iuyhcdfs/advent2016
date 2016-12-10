#!/usr/bin/python3.5

import sys

# if youre going left to right, 
# youll match the thing if it has happened before or after so dont worry
# theres no invalidating condition in part 2.

numValid = 0
# youre just comparing last 4 chars. way simpler than dictionary index
for line in sys.stdin:
    inBrack = {}
    noBrack = {}
    hasSSL = 0
    inBracket = 0
    for i in range(2, len(line)):
        # continues prevent the [.] issue
        if inBracket == 0 and line[i] == '[':
            inBracket = 1
            continue 
        if inBracket == 1 and line[i] == ']':
            inBracket = 0
            continue
        if line[i] == line[i-2] and line[i] != line[i-1]:
            if inBracket == 1:
                inBrack[line[i] + line[i-1]] = 1
            if inBracket == 0:
                noBrack[line[i-1] + line[i]] = 1
    for key in noBrack:
        for yek in inBrack:
            if key[0] == yek[0] and key[1] == yek[1]:
                hasSSL = 1
    if hasSSL == 1:
        numValid += 1

print(numValid)
