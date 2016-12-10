#!/usr/bin/python3.5

# go along each hash, with a tail end int increasing

# check if hash has 5 leading zeroes.
# record first character.

# do it eight times.

tailIndex = 0
password = [0,0,0,0,0,0,0,0]

import sys
import hashlib

puzzleInput = b'ugkcyxxp'
done = [0,0,0,0,0,0,0,0]

while done != [1,1,1,1,1,1,1,1]:
    h = hashlib.md5()
    #print(tailIndex)
    #print(password)
    h.update(puzzleInput + str(tailIndex).encode('utf-8'))
    digest = h.hexdigest()
    for i in range(0,6):
        if i == 5:
            if '0' <= digest[5] <= '7':
                diglett = int(digest[5])
                if done[diglett] == 0:
                    password[diglett] = digest[6]
                    done[diglett] = 1
        if digest[i] != '0':
            break
    tailIndex += 1
print(password)
