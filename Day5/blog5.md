---
title: "AoC 2022 - Day 5"
aliases: ["blog5", "Advent of Code 2022 - Day 5"]
tags: "python"
---

# Advent of Code: Day 5

## Supply Stacks
[Original Problem on AoC](https://adventofcode.com/2022/day/5)


Awe hell yeah, time to experiment with the curses library. Gonna make a visual for this one, and it's going to be sweet (AT LEAST functional)
...
Okay, maybe later. This one took a while. But I've come across some neat libraries I can implement here, so I will circle back to this for a fun learning experience. Here's what I gather can be improved upon in future:
    - Use curses to animate this
    - Use numpy to be performant
    - Use perfcounter to confirm numpy is more performant
    - Make Object-Oriented design better
    - Use modulus and list comprehension where sensible
    - Use map where I can

Okay, part 2 -- they maintain the same order. I'll either sort the crate_escrow before placing them in, or reverse that quantity on the destination stack after each movement.
I've also used the debugger approx zero times, so I should probably do that. I would hover over a variable to view the data type, realize it gets loaded at runtime, then say fug it, I'll just print it with type() or take a shotgun approach... not great. 
