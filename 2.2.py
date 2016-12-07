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
keypad['A'] = {}
keypad['B'] = {}
keypad['C'] = {}
keypad['D'] = {}

keypad[1]['U'] = 1
keypad[1]['D'] = 3
keypad[1]['L'] = 1
keypad[1]['R'] = 1

keypad[2]['U'] = 2
keypad[2]['D'] = 6
keypad[2]['L'] = 2
keypad[2]['R'] = 3

keypad[3]['U'] = 1 
keypad[3]['D'] = 7
keypad[3]['L'] = 2
keypad[3]['R'] = 4

keypad[4]['U'] = 4
keypad[4]['D'] = 8
keypad[4]['L'] = 3
keypad[4]['R'] = 4

keypad[5]['U'] = 5
keypad[5]['D'] = 5
keypad[5]['L'] = 5
keypad[5]['R'] = 6

keypad[6]['U'] = 2
keypad[6]['D'] = 'A'
keypad[6]['L'] = 5
keypad[6]['R'] = 7

keypad[7]['U'] = 3
keypad[7]['D'] = 'B'
keypad[7]['L'] = 6
keypad[7]['R'] = 8

keypad[8]['U'] = 4
keypad[8]['D'] = 'C'
keypad[8]['L'] = 7
keypad[8]['R'] = 9

keypad[9]['U'] = 9
keypad[9]['D'] = 9
keypad[9]['L'] = 8
keypad[9]['R'] = 9

keypad['A']['U'] = 6
keypad['A']['D'] = 'A'
keypad['A']['L'] = 'A'
keypad['A']['R'] = 'B'

keypad['B']['U'] = 7
keypad['B']['D'] = 'D'
keypad['B']['L'] = 'A'
keypad['B']['R'] = 'C'

keypad['C']['U'] = 8
keypad['C']['D'] = 'C'
keypad['C']['L'] = 'B'
keypad['C']['R'] = 'C'

keypad['D']['U'] = 'B'
keypad['D']['D'] = 'D'
keypad['D']['L'] = 'D'
keypad['D']['R'] = 'D'

digit = 5
sequence = ""

for string in array:
    for char in string:
        digit = keypad[digit][char]
    sequence += str(digit)

print(sequence)
