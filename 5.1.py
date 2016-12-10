#!/usr/bin/python3.5

# go along each hash, with a tail end int increasing

# check if hash has 5 leading zeroes.
# record first character.

# do it eight times.

tailIndex = 0
password = ''

import sys
import hashlib

puzzleInput = b'ugkcyxxp'

while len(password) < 8:
    h = hashlib.md5()
    #print(tailIndex)
    #print(password)
    h.update(puzzleInput + str(tailIndex).encode('utf-8'))
    digest = h.hexdigest()
    for i in range(0,6):
        if i == 5:
            password += digest[i]
        if digest[i] != '0':
            break
    tailIndex += 1
print(password)
