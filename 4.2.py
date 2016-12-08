#!/usr/bin/python3.5

import sys
import re

answer = 0

for stdl in sys.stdin:
    m = re.match(r"^(.*)-(...)\[(.....)\]$", stdl)
    if m:
        dictionary = {}
        chars = re.sub(r"-",
                       r"",
                       m.group(1))
        for ch in chars:
            if ch in dictionary:
                dictionary[ch] += 1
            else:
                dictionary[ch] = 1
        
        #for keys in sorted(dictionary):
        results = sorted(dictionary.items(), key = lambda x: (-x[1],x[0]))
        code = ""
        for i in range(0,5):
            code += results[i][0]

        if code == m.group(3):
            # just rotate by m.group(2)



