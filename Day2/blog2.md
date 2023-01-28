
# Advent of Code: Day 2
## Rock Paper Scissors
[Original Problem on AoC](https://adventofcode.com/2022/day/2)



For too long I couldn't figure out why my function wasn't working. I was checking for X,Y,Z first, because I associated it with the opponent (who I knew was represented by the first column). After figuring that out, I then assumed we wanted to grab both my score and the opponent's score, so returned an array, so I overshot this one. But we got there.

And then I realized I was only returning the score for the result, not for the shape used....


For the second part I decided I didn't need to change my function, because why not just add a wrapper that determines what I need to provide for my_move, and then pass that along. For that function, I just created some dictionaries that mapped moves based on the outcome I needed. Probably a better codegolf way of implementing this, but I like readability. And I'm a bad coder.