#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/5
No space left on device

Part 1: 
    - Determine directory structure and size based on commands issued.
    - 123 abc means file called 'abc' 
    - dir e means current directory contains dir named e

To Solve:
    - Find directories with at least 100000, provide sum all of those directories.

Strategy:
    - Create Dictionary with directorys as Keys and Files as values.
    - Store the keys as absolute paths

"""


import logging


location = [] # location is current path
buffer = []
#filesystem = ["/"]

# Store directories as keys, lists of dir and files within directory as list.
filesystem = {
    '/': []
}

# sloppy, but going to track sizes in this dictionary
dir_sizes = {
    '/': 0
}


#path = "/home/user/AoC2022/Day6/input.lst"
path = "/home/user/Projects/Python/AoC2022/Day7/input.lst"
logpath = "/home/user/Projects/Python/AoC2022/Day7/traceback.log"
#cgitb.enable(logdir=logpath)

logging.basicConfig(level=logging.DEBUG)

def find_sum(a_dictionary_object):
    sum = 0
    logging.info('Beginning Sum Function')
    # print(a_dictionary_object)
    for key in a_dictionary_object.keys():
        
    #print(item)
        if a_dictionary_object[key] <= 100000:
            logging.info(f'The key is: {key}')
            logging.info(f'Above key has total size: {a_dictionary_object[key]}')
            sum += a_dictionary_object[key]
        else:
            pass

    return sum



with open(path) as rucksack_file:
    for row in rucksack_file:
        word = row.split()

        if word[0] == "$":
            match word[1]:
                case "cd":
                    logging.info(f'Word = {word}')

                    # If go back a directory, remove last value from location list
                    if word[2] == "..":
                        # remove last value from current path
                        location.pop()
                        
                    elif word[2] == "/":
                        location = ["/"]

                    else:
                        # check if already known key in dictionary (so we know whether to add to value type list, or just new list)
                        if word[2] not in dir_sizes:
                            # add new dir/file to filesystem, update location
                            dir_sizes[word[2]] = 0
                            
                        else:
                            # if already known, just change location.
                            pass
                        location.append(word[2])
                    logging.info(f"Location is now {location}")

                case "ls":
                    pass
        

        # If dir or numbers, doesn't matter -- either way we only care about word after it
        elif word[0] == 'dir':
            # Check if dir already known
            if word[1] not in dir_sizes:
                dir_sizes[word[1]] = 0
                
                # Need to check if this dir exists underneath current directory
            else:
                pass
        else: # if not dir, then it's a file, and so the first value is the file size
            logging.info((f'filename: {word[1]}, filesize: {word[0]}'))
            # add this file to the current location..., wait, why was I doing that?
            # filesystem[location[-1]].append(word[1])

            # Add size to all directorys in path
            for i in location:
                # Check if in dictionary, add if not
                if i not in dir_sizes:
                    dir_sizes[i] = int(word[0])
                else:
                    dir_sizes[i] += int(word[0])  
                
                logging.info(f'Added {word[0]} to dir {i}')
         
            #print(word)
            

print(find_sum(dir_sizes))
#print(f'Dir Sizes: {dir_sizes}')


