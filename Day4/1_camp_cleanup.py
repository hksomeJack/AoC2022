#!/usr/bin/env python3


"""
https://adventofcode.com/2022/day/4
Fix the elve's poor rucksack-packing job.

Part 1: 
    Elves need to clean up camp sections. 
    Input shows elf pairs, where each elve's range is the Section IDs they are responsible.
    Lots of overlap between elf pairs, meaning lots of duplicate work.
    Need to prioritize a reassignment of cleaning duties by finding elves whose cleaning assignment is fully contained within their pair elf's.
To solve:
    Find elf groups where one elf's range is fully contained within another; 
    Tally the number of these instances you find.
"""
# TEST CASES
# Doesn't fully contain
x = range(1,10)
y = range(8,20)

# DOES full contain
x2 = range(10, 20)
y2 = range(15, 17)


pairs = 0


def compare_range(first,second):

    # Find max from the Start of both ranges, then find the min of the End of both ranges
    #elf1 = first.
    #print(f"First: {first}")
    #print(f"{first[0]}")
    overlap = range(max(first[0], second[0]), min(first[-1], second[-1])+1)
    #print(f"Overlap: {overlap}")
    #print(f"Elf1: {first}")
    
    # Check if the overlap is exactly the range of either elf.
    if overlap == first or overlap == second:
        return 1
    else:
        return 0
    #   print(f"Either {first} or {second} is equal to {overlap}")


with open('/Users/user/Projects/Python/AoC2022/Day4/input.lst') as rucksack_file:
    for row in rucksack_file:
        elves = row.split(',')

        # Need to add 1 her because only Start is inclusive in Python's range function.
        elf1 = range(int(elves[0].split('-')[0]), int(elves[0].split('-')[1])+1)
        elf2 = range(int(elves[1].split('-')[0]), int(elves[1].split('-')[1])+1)

        #print(f"Elf1: {elf1[0]}")
        #print(f"Elf2: {elf2[0]}")
        pairs += compare_range(elf1, elf2)


    print(pairs)