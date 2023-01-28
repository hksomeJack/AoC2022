#!/usr/bin/env python3


'''
https://adventofcode.com/2022/day/2
Rock Paper Scissors simulation that takes predetermined inputs.

Part 1
    Assumes the input codes:
        First column is opponent's move:
            X for Rock, Y for Paper, and Z for Scissors.
        Second column is your move:
            A for Rock, B for Paper, and C for Scissors.
            
    Score Calculation (per round):  
        1 for Rock, 2 for Paper, and 3 for Scissors
        +
        0 for loss, 3 for draw, 6 for win
    
    Scores are cumulative.
    Determine who wins given the predetermined input.

Part 2
    Actually:
        X means you should lose
        Y means you should draw
        Z means you should win
'''

opponent_score = 0
my_score = 0

def play_game(opponent_move, my_move):

    # Determine outcome of game, then return the score for that output.
    if opponent_move == 'A':
        if my_move == 'X':
            return [4,4]
        if my_move == 'Y':
            return [1,8]
        if my_move == 'Z':
            return [7,3]
    elif opponent_move == 'B':
        if my_move == 'X':
            return [8,1]
        if my_move == 'Y':
            return [5,5]
        if my_move == 'Z':
            return [2,9]
    elif opponent_move == 'C':
        if my_move == 'X':
            return [3,7]
        if my_move == 'Y':
            return [9,2]
        if my_move == 'Z':
            return [6,6]


with open('/Users/user/Projects/Python/AoC2022/Day2/rps_input.lst') as rps_file:
    for row in rps_file:
        moves_this_turn = row.split()
        

        # Store result so function just runs once, then access variables in array
        result = play_game(moves_this_turn[0], moves_this_turn[1])
        
        opponent_score += result[0]
        my_score += result[1]

    rps_file.close()

print("Opponent score is: " + str(opponent_score))
print("My Score is: " + str(my_score))