#!/usr/bin/env python3

'''
Calorie Counter:
    Each elf is carrying food. 
    Each individual food item is represented by its caloric value.
    Each elve's inventory is separated by a newline.
    The "most" food is determined by highest total calories.
    
    Given an input as described above, this program determines
        how many calories the elf is carrying that is carrying
        the most food.
'''


# Read calories
calories_list = {}
counter = 0

# Initialize list with 0 as the firstkey
calories_list[counter] = []

# list that will contain total calorie count for each elf
total_calories_list = {}

max_value = 0

with open('/Users/user/Projects/Python/AoC2022/Day1/calories.lst') as calories_file:

    # calories_content = calories_file.readlines()
    for row in calories_file:
        
        # If this isn't a newline, add to our current nested list (exists because initialized above)
        if row != '\n':
            calories_list[counter].append(int(row.strip()))
        else:

            # if encounter newline, sum values gathered for this dict key, and store in total_calories_list
            total_calories_list[counter] = sum(calories_list[counter])

            # Create new key for next elf
            counter+=1
            calories_list[counter] = []

    # Determine the largest value
    for i in range(len(total_calories_list)):
        #print(total_calories_list[i])
        if total_calories_list[i] > max_value:
            max_value = total_calories_list[i]
        else:
            continue
   
        
print(max_value)
