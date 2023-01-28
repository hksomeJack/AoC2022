
# Advent of Code: Day 4
## Camp Cleanup
[Original Problem on AoC](https://adventofcode.com/2022/day/4)


# Part 1

Because I'm bad, I started using some if statements. I wanted to explore the logic before taking advantage of Python methods, so I decided I would find out the lowest value and the highest value in a pair, and find all cases where both these values are owned by one of the elves in the pair (meaning that elf fully encapsulates the other).

After that, I was reminded of just using sets again to make that determination, but after a quick Googe for overlap, I see that I can just use range to the same (although perhaps more performative) effect.


# Part 2

Looks like Part 2 is as expected -- we can't get away with just taking out the full overlaps, we want all overlaps. Good thing we accounted for this in our original program, woohoo.

We'll remove the check for full overlap, which was just finding an overlap that corresponded to either elve's range.

```python
if overlap == first or overlap == second:
        return 1
    else:
        return 0
```


