#!/usr/bin/env python3

'''
Calorie Counter:
    Each elf is carrying food. 
    Each individual food item is represented by its caloric value.
    Each elve's inventory is separated by a newline.
    The "most" food is determined by highest total calories.
    
    Given an input as described above, this program determines
        how many calories are being carried by the top 3 elves in total.
'''


# Read calories
calories_per_item = {}
counter = 0

# Initialize list with 0 as the first key
calories_per_item[counter] = []

# list that will contain total calorie count for each elf
calories_per_elf = {}

# For max value in total_calories_list
max_value = []

with open('/Users/user/Projects/Python/AoC2022/Day1/calories.lst') as calories_file:

    # calories_content = calories_file.readlines()
    for row in calories_file:
        
        # If this isn't a newline, add to our current nested list (exists because initialized above)
        if row != '\n':
            calories_per_item[counter].append(int(row.strip()))
        else:
            # if encounter newline, sum values gathered for this dict key, and store in total_calories_per_item
            calories_per_elf[counter] = sum(calories_per_item[counter])

            # Create new key for next elf
            counter+=1
            calories_per_item[counter] = []
        



# Determine the sum of the 3 largest values
sorted_calories_per_elf = sorted(calories_per_elf.values(), reverse=True)
print(sum(sorted_calories_per_elf[:3]))
#top3 = sort

