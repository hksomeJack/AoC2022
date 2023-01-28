#!/usr/bin/env python3


"""
https://adventofcode.com/2022/day/3
Fix the elve's poor rucksack-packing job.

Part 1:
    - All items of a given type go into exactly one of the two compartments in a rucksack
    - The packing elf failed to do this for exactly one item type per rucksack
    - Item types are identified by single uppercase or lowercase letter 
        - i.e., 'a' and 'A' are different
    - Each line represents a rucksack, where the first half is compartment 1, second is compartment 2.
        - if either share the same cap-sensitive character, that means that item is in both compartments.

    To prioritize item rearrangement, items are given the following priorities.
        - a-z: 1-26
        - A-Z: 27-52


    To Solve: 
        Find the item shared between both compartments in each rucksack, sum the priorities of each.
"""

common_characters = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'

sum = 0

def get_priority(target_character):

    if (target_character.upper() == (target_character)):
        priority = alphabet.find(target_character.lower()) + 27
    else:
        priority = alphabet.find(target_character) + 1

    return priority
        

with open('/Users/user/Projects/Python/AoC2022/Day3/inputs.lst') as rucksack_file:
    for row in rucksack_file:
        
        # Get the contents of both compartments (first half and last half, respectively)
        compartment1 = row[0 : int((len(row)/2))]
        compartment2 = row[int((len(row)/2)) : int(len(row))]

        #common_character = list(set(compartment1)&set(compartment2))
        # Sets can't have duplicates
        common_characters.append(list(set(compartment1)&set(compartment2)))
        
        
    
    for i in range(len(common_characters)):
        sum += get_priority(common_characters[i][0])
        print("Priority of " + str(common_characters[i][0]) + " is: " + str(get_priority(common_characters[i][0])))



print(sum) 


        


