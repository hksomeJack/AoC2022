#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/5
Supply Stacks.

Part 1: 
    Fix the elve's communication deceive.
    Receives signal (alphabeical string), needs subroutine to detect start-of-packet marker
    Marker is 4 unique characters (none repeating).

To solve: 
    Report number from characters from beginning of input to end of Marker.

Strategy:
    Try adding each next 4 sequence to set, exception means repeating. Find first success, then take index of variable storing input

"""

class CustomException(Exception):
    pass


#path = "/home/user/AoC2022/Day6/input.lst"
path = "/Users/user/Projects/Python/AoC2022/Day6/input.lst"

signal = ""

buffer = []

#signal = 'asddfdrrdftg'
with open(path) as rucksack_file:
    for row in rucksack_file:
        signal = row

        # Store first four so we can step consistently in loop below
        #buffer = signal[0:3]

        for i in range(len(signal)):
            buffer = signal[i:i+14]
            # split into strings using the unpack method *
            check = {*buffer}
            if len(check) == 14:
                print(f"Unique: {check}")
                print(f"Found {i+14} characters deep")
                break




            
            
