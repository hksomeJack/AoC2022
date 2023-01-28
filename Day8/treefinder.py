#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/8
Treetop Tree House

"""

import logging
# import numpy as np


sum = 0
forest = []
visibility_map = []
counter = 0
path = "/home/user/Projects/Python/AoC2022/Day8/input.lst"

# Enable logging
logging.basicConfig(level=logging.DEBUG)

# Read each line into nested arrays 'forest'
with open(path) as rucksack_file:

    # Read every line into a list. THis is our forest.
    forest = rucksack_file.readlines()

# Convert all visible trees to 1, obscured trees to 0
def determine_visibility(a_forest):

    
    rows = len(a_forest)

    # Assuming it's a square, just sample first row
    columns = len(a_forest[0])

    # Read rows from list, create visibility map from it
    for row_index in range(rows):
        # If these are horizontal edge trees, set whole row to 1

        logging.info(f"Row: {a_forest[row_index]}")
        if row_index == 0:
            visibility_map[0].append(int(columns*'1'))
            for tree_index in range(columns):
                visibility_map[tree_index].append([0][tree_index])
                logging.info("First row")
        
        # If this is the last row, set whole row to 1
        elif row_index == rows:
            for tree in range(len(a_forest[row_index])):
                visibility_map[row_index]
                logging.info("Last row")
        # Not first or last row, so just set first and last values to 1
        else:
            pass

        logging.info(f"Length of column: {columns}")
        logging.info(f"Row is: {a_forest[row_index]}")

    return visibility_map

print(determine_visibility(forest))
    
