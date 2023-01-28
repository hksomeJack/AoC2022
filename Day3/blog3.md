
# Advent of Code: Day 3
## RuckSack Reorganization
[Original Problem on AoC](https://adventofcode.com/2022/day/3)


Today, my first fool1sh move was to import the python program instead of the inputs, and then I couldn't figure out why my shebang line kept getting printed. Yeesh.

Alright, let's figure out a plan of attack. 

First, grab the compartments (first and last half of string).
Now, can we compare strings easily in Python? We could try using difflib, or maybe even compare sets in a list. Quick reminder on the 4 multivalue data types in Python, taken from a different site:

    "List is a collection which is ordered and changeable. Allows duplicate members.
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    Dictionary is a collection which is ordered** and changeable. No duplicate members."

Let's try using the list() and set() constructors to make a list containing the common charaacters between the two. I found this nuggest at: https://www.sanfoundry.com/python-program-check-common-letters-string

'''python
        rucksack = list(set(compartment1)&set(compartment2))
'''

That worked, so how about just adding to this array, then summing it based on a map of priorities.

And then I realized that I didn't have to generate a map, since I can just get the inde (using the string find() method) and add 1 (or 27 if upper)


Part 2:
let's use sets again, except let's employ a switch statement. This is newish to Python, where before people were using dictionaries.
