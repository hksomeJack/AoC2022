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


# Maps how to lose using opponent's move as key
lose_map = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}

# same...
draw_map = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

# same... 
win_map = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'

}


def determine_move(opp_move, outcome_needed):
    if outcome_needed == 'X':
        return lose_map[opp_move]
    if outcome_needed == 'Y':
        return draw_map[opp_move]
    if outcome_needed == 'Z':
        return  win_map[opp_move]
        




def play_game(opponent_shape, my_shape):
    # Determine outcome of game, then return the score for that output.
    if opponent_shape == 'A':
        if my_shape == 'X':
            return [4,4]
        if my_shape == 'Y':
            return [1,8]
        if my_shape == 'Z':
            return [7,3]
    elif opponent_shape == 'B':
        if my_shape == 'X':
            return [8,1]
        if my_shape == 'Y':
            return [5,5]
        if my_shape == 'Z':
            return [2,9]
    elif opponent_shape == 'C':
        if my_shape == 'X':
            return [3,7]
        if my_shape == 'Y':
            return [9,2]
        if my_shape == 'Z':
            return [6,6]


with open('/Users/user/Projects/Python/AoC2022/Day2/rps_input.lst') as rps_file:
    for row in rps_file:
        strategy = row.split()

        opponent_move = strategy[0]
        #print("Opp move: " + opponent_move)
        my_move = determine_move(opponent_move, strategy[1])
        #print("My move: " + my_move)
        points_awarded = play_game(opponent_move, my_move)
        #print(play_game(opponent_move, my_move))
       
        opponent_score += points_awarded[0]
        my_score += points_awarded[1]

print("Opponent score is: " + str(opponent_score))
print("My Score is: " + str(my_score))