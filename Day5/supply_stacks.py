#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/5
Supply Stacks.

Part 1: 
    Rearrange crates according to instructions. Like a paint-by-numbers hanoi tower.
    Each instruction is to move quantity of crates from one stack to another.

Part 2:
    Same deal, but moving the whole quantity of crates at once, so they remain in the same order

Future improvements: 
    - Use curses to animate this
    - Use numpy to be performant
    - Use perfcounter to confirm numpy is more performant
    - Make Object-Oriented design better
    - Use modulus and list comprehension where sensible
    - Use map where I can
   
"""

import re


# Initial list
all_rows = []

# nested lists with all stacks/items
crates = []

# All instructions (that which follows the blank line, aka \n)
instructions = []

# Dictionary for storing stack objects
stack_objects = {}

# Used to obtain dimensions of stacks (height and width)
counter = 0

path = "/home/user/AoC2022/Day5/input.lst"
# path = '/Users/garretdonaldson/Projects/Python/AoC2022/Day5/input.lst'

# Start by getting all inputs, because I suck at programming
with open(path) as rucksack_file:
    for row in rucksack_file:

        # Get horizontal axis length so we know how many stacks there are.
        # Each element consists of 3 characters followed by a space, except the last, which is followed by a newline.
        # So we divide by 4 to get the number of stacks.
        # Only do this for first row, so we can lock it in.
        #if counter == 0:
        #   stacks = len(row) / 4 # maybe use modulus here, do some clock arithmetic?

        # Grab crate stack, delimited by the line break.
        if row != '\n':
            all_rows.append(row)
            counter += 1
        # Once reached, capture dimension
        else:
            #Use counter to measure height, -1 because not counting stack label.
            stack_height = counter - 1
            stack_width = counter


def get_crates(height):
    crate_list = all_rows[0:height+1]
    return crate_list

def get_instructions(height):
    instruction_list = all_rows[height:]
    del instruction_list[0]

    # Parse out digits from instruction list
    for i in range(len(instruction_list)):
        instruction_list[i] = re.findall("\d?\d", instruction_list[i])

    return instruction_list
        
def get_items_by_stack_label(stack_label):

        # Last array is the stack index. Grab that.
        stack_index = crates[-1]
        stack_contents = []

        # Use stack label to find the character at the list index corresponding to that label 
        # e.g., stack_index has stack 2 at index 5, so find all characters at index 5 in each row.
        for i in crates:
            item = i[stack_index.index(stack_label)]

            # Tentative, because maybe we want to reserve space to make moving easier.
            if item != ' ':
                stack_contents.append(item)
        # Remove index value from end of list
        #stack_contents.pop()
        return stack_contents
    
def move_items_between_stacks(quantity, source, destination):
    '''
    source and destination refer to Stack object instances, quantity is an int.
    '''
    # Grab slice of crates that need moving (descending from top of stack), then remove from stack object's item list
    crate_escrow = source.items[0:(quantity)]
    print(crate_escrow)

    #  Simple addition for Part 2 -- reverse so that we simulate the crane grabbing multiple crates at once
    crate_escrow.reverse()

    #print(f"Source items before: {source.items}")
    source.remove_items(quantity)
    #print(f"Removed: {crate_escrow}")
    #print(f"Source items after: {source.items}")


    #print(f"Destination items before:{destination.items}")
    destination.add_items(crate_escrow)
    #print(f"Destination items after: {destination.items}")

class Stack:
    """
    This class operates on the global 'Crates' array
    """

    def __init__(self, label):
        self.label = label

        
        self.items = get_items_by_stack_label(self.label)

        # Pop (remove) last value, since this is the index. We only need index for the get_items... function
        self.items.pop()

    # Crates are in descending order (from top of stack to bottom)
    def remove_items(self, quantity):
        del self.items[0:quantity]


    def add_items(self, crates_being_moved):
        for i in crates_being_moved:
            self.items.insert(0, i)

# Split all_rows into the two relevant lists: crates and instructions
crates= get_crates(stack_height)
instructions = get_instructions(stack_height)


# Create dictionary of stack objects
for i in range(stack_height+1):
    key = "stack" + str(i+1)
    value = Stack(str(i+1))
    stack_objects[key] = value

print(f"Stack1 before: {stack_objects['stack1'].items}")
print(f"Stack2 before: {stack_objects['stack2'].items}")
print(f"Stack3 before: {stack_objects['stack3'].items}")
print(f"Stack4 before: {stack_objects['stack4'].items}")
print(f"Stack5 before: {stack_objects['stack5'].items}")
print(f"Stack6 before: {stack_objects['stack6'].items}")
print(f"Stack7 before: {stack_objects['stack7'].items}")
print(f"Stack8 before: {stack_objects['stack8'].items}")
print(f"Stack9 before: {stack_objects['stack9'].items}")

for i in range(len(instructions)):
    #print(f"Move {instructions[i][0]} from stack{instructions[i][1]} to stack{instructions[i][2]}")
    move_items_between_stacks(int(instructions[i][0]), stack_objects[f"stack{(str(instructions[i][1]))}"], stack_objects[f"stack{(str(instructions[i][2]))}"])

print(f"\n\nStack1 after: {stack_objects['stack1'].items}")
print(f"Stack2 after: {stack_objects['stack2'].items}")
print(f"Stack3 after: {stack_objects['stack3'].items}")
print(f"Stack4 after: {stack_objects['stack4'].items}")
print(f"Stack5 after: {stack_objects['stack5'].items}")
print(f"Stack6 after: {stack_objects['stack6'].items}")
print(f"Stack7 after: {stack_objects['stack7'].items}")
print(f"Stack8 after: {stack_objects['stack8'].items}")
print(f"Stack9 after: {stack_objects['stack9'].items}")


 


    