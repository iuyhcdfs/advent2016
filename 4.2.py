#!/usr/bin/python3.5

import sys
import re

answer = 0

def rot(char):
    if char == 'z' or char == 'Z' :
        return chr( ord(char) - 25 )
    else:
        return chr( ord(char) + 1 )


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
        
        results = sorted(dictionary.items(), key = lambda x: (-x[1],x[0]))
        code = ""
        for i in range(0,5):
            code += results[i][0]

        if code == m.group(3):
            decrypt = ''
            for ch in chars:
                for x in range(0,int(m.group(2))):
                    ch = rot(ch)
                decrypt += ch
            print(decrypt + ' has sector id ' + m.group(2))


                 
