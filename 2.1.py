#!/usr/bin/python3.5

import sys

debug = 1

lines = sys.stdin.read()
array = lines.splitlines()

keypad = {}
keypad[1] = {}
keypad[2] = {}
keypad[3] = {}
keypad[4] = {}
keypad[5] = {}
keypad[6] = {}
keypad[7] = {}
keypad[8] = {}
keypad[9] = {}

keypad[1]['U'] = 1 
keypad[1]['D'] = 4
keypad[1]['L'] = 1
keypad[1]['R'] = 2

keypad[2]['U'] = 2
keypad[2]['D'] = 5
keypad[2]['L'] = 1
keypad[2]['R'] = 3

keypad[3]['U'] = 3 
keypad[3]['D'] = 6
keypad[3]['L'] = 2
keypad[3]['R'] = 3

keypad[4]['U'] = 1
keypad[4]['D'] = 7
keypad[4]['L'] = 4
keypad[4]['R'] = 5

keypad[5]['U'] = 2
keypad[5]['D'] = 8
keypad[5]['L'] = 4
keypad[5]['R'] = 6

keypad[6]['U'] = 3
keypad[6]['D'] = 9
keypad[6]['L'] = 5
keypad[6]['R'] = 6

keypad[7]['U'] = 4
keypad[7]['D'] = 7
keypad[7]['L'] = 7
keypad[7]['R'] = 8

keypad[8]['U'] = 5
keypad[8]['D'] = 8
keypad[8]['L'] = 7
keypad[8]['R'] = 9

keypad[9]['U'] = 6
keypad[9]['D'] = 9
keypad[9]['L'] = 8
keypad[9]['R'] = 9

digit = 5
sequence = ""

for string in array:
    for char in string:
        digit = keypad[int(digit)][char]
    sequence += str(digit)

print(sequence)
