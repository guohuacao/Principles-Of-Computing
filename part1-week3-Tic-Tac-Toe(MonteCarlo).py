"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 100         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

# TTTBoard constants
# provided.EMPTY
# provided.PLAYERX
# provided.PLAYERO
# provided.DRAW
# provided.switch_player(player)

def mc_trial(board, player):
    """
    Input board, start game with input player by random play
    rotate between player, modify board. return when game over
    """
    #b_dim = board.get_dim()
    while (board.check_win() == None):
        empty_list = board.get_empty_squares();
        # print empty_list
        player_move = random.choice(empty_list)
        board.move(player_move[0],player_move[1], player)
        if ( player == provided.PLAYERX):
            player = provided.PLAYERO
        else:
            player = provided.PLAYERX

    #print board.__str__()
    return


def mc_update_scores(scores, board, player):
    """
    update scores(a grid of score as the dimention of the board
    """
    b_dim = board.get_dim()
    winner = board.check_win()
    if ( winner == provided.PLAYERX ):
        other = provided.PLAYERO
        for col in range(b_dim):
            for row in range(b_dim):
                if (board.square(row, col) == winner):
                    scores[row][col] += SCORE_CURRENT
                elif (board.square(row,col) == other):
                    scores[row][col] -= SCORE_OTHER
                elif (board.square(row,col) == provided.EMPTY):
                    scores[row][col] += 0

        #print scores
    elif ( winner == provided.PLAYERO ):
        other = provided.PLAYERX
        for col in range(b_dim):
            for row in range(b_dim):
                if (board.square(row, col) == winner):
                    scores[row][col] += SCORE_CURRENT
                elif (board.square(row, col) == other):
                    scores[row][col] -= SCORE_OTHER
                elif (board.square(row, col) == provided.EMPTY):
                    scores[row][col] += 0
        #print scores
    print "scores for games so far: ", scores
    return



def get_best_move(board, scores):
    """
    when board is not empty, return (row, column)tuple for best move
    random if there is more than one for the best move
    """
    best_scores = []
    b_dim = board.get_dim()
    empty_list = board.get_empty_squares();
    if (not empty_list):
        return
    empty_squre = random.choice(empty_list)

    value = scores[empty_squre[0]][empty_squre[1]]
    for col in range(b_dim):
        for row in range(b_dim):
            if (scores[row][col] ==  value):
                if ((row,col) in empty_list):
                    best_scores.append((row, col))
            elif (scores[row][col] >  value):
                if ((row,col) in empty_list):
                    best_scores = []
                    best_scores.append((row, col))
                    value = scores[row][col]

    print best_scores
    return random.choice(best_scores)


def mc_move(board, player, trials):
    """
    Implement MC method for best move, return (row, column)tuple
    my_score is 3x3 grid
    ie
    """
    b_dim = board.get_dim()
    print board.__str__()
    mc_score=[[0 + 0 for dummy_col in range(b_dim)]
                           for dummy_row in range(b_dim)]

    mc_board = board.clone()
    for dummy in range(trials):
        mc_trial(mc_board, player)
        mc_update_scores(mc_score, mc_board, player)

    print mc_score
    return get_best_move(board, mc_score)



# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
# mov = get_best_move(provided.TTTBoard(2, False, [[provided.EMPTY, provided.EMPTY], [provided.EMPTY, provided.EMPTY]]), [[0, 0], [3, 0]])
# print mov
# mov = get_best_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], [provided.PLAYERO, provided.PLAYERX, provided.PLAYERX], [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]]), [[0, 2, 0], [0, 2, 0], [0, 2, 0]])
# print mov
#mov = get_best_move(provided.TTTBoard(3, False, [[provided.EMPTY, provided.PLAYERX, provided.EMPTY], [provided.PLAYERO, provided.PLAYERX, provided.EMPTY], [provided.PLAYERO, provided.EMPTY, provided.EMPTY]]), [[-3, 6, -2], [8, 0, -3], [3, -2, -4]])
#print mov
#mov = get_best_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], [provided.PLAYERO, provided.PLAYERX, provided.PLAYERX], [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]]), [[3, 2, 5], [8, 2, 8], [4, 0, 2]])
#print mov
#mc_trial(provided.TTTBoard(2, False, [[provided.EMPTY, provided.EMPTY], [provided.EMPTY, provided.EMPTY]]), 2)
#mc_trial(provided.TTTBoard(2, False, [[provided.EMPTY, provided.EMPTY], [provided.EMPTY, provided.EMPTY]]), 2)
#mc_update_scores([[0, 0, 0], [0, 0, 0], [0, 0, 0]], provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], [provided.PLAYERO, provided.PLAYERX, provided.EMPTY], [provided.EMPTY, provided.PLAYERX, provided.PLAYERO]]), 2)
#mc_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], [provided.EMPTY, provided.PLAYERX, provided.PLAYERX], [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]]), provided.PLAYERO, NTRIALS)
#mc_move[provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], [provided.EMPTY, provided.PLAYERX, provided.PLAYERX], [provided.PLAYERO, provided.PLAYERO, provided.PLAYERO]]), 3, 1, [(2, 1)]]
#mc_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], [provided.PLAYERO, provided.PLAYERX, provided.PLAYERX], [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]]), provided.PLAYERX, NTRIALS)
#mc_move(provided.TTTBoard(3, False, [[provided.EMPTY, provided.PLAYERX, provided.PLAYERX], [provided.PLAYERO, provided.EMPTY, provided.PLAYERX], [provided.PLAYERO, provided.PLAYERX, provided.EMPTY]]), provided.PLAYERO, NTRIALS)
#mc_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.EMPTY, provided.EMPTY], [provided.PLAYERO, provided.PLAYERO, provided.EMPTY], [provided.EMPTY, provided.PLAYERX, provided.EMPTY]]), provided.PLAYERX, NTRIALS)
#mc_update_scores([[0, 0, 0], [0, 0, 0], [0, 0, 0]], provided.TTTBoard(3, False, [[provided.PLAYERX, provided.EMPTY, provided.EMPTY], [provided.EMPTY, provided.PLAYERX, provided.PLAYERX], [provided.PLAYERO, provided.PLAYERO, provided.PLAYERO]]), 2)
