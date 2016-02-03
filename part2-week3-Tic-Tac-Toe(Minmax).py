"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

print 'x ',provided.PLAYERX
print 'o ',provided.PLAYERO
print 'd ',provided.DRAW
#x  2
#o  3
#d  4
def mm_move(board, player):
    """
    Make a move on the board.

    Returns a tuple with two elements.
    The first element is the score
    of the given board and the second element is
    the desired move as a
    tuple, (row, col).
    """
    other_player = provided.switch_player(player )
    # Base Cases
    if board.check_win() == provided.PLAYERX:
        return 1,(-1,-1)
    elif board.check_win() == provided.DRAW:
        return 0,(-1,-1)
    elif board.check_win() == provided.PLAYERO:
        return -1,(-1,-1)
    # If Game in Progress
    elif board.check_win() == None:
        best_score = 0
#        if player == provided.PLAYERO:
#            best_score = 5000
#        else:
#            best_score = -5000
        grand_scores = []
        grand_moves = []
        for move in board.get_empty_squares():
            dum_board = board.clone()
            dum_board.move(move[0],move[1],player)
            m_option = mm_move (dum_board, other_player)
            grand_scores.append(m_option[0])
            grand_moves.append(move)
            if m_option[0] == SCORES[player]:
                    return m_option[0],move
        if player == provided.PLAYERX:
            best_score = max(grand_scores)
        else :
            best_score = min(grand_scores)
        best_index=grand_scores.index(best_score)
        return grand_scores[best_index],grand_moves[best_index]



def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

#unit_test.test_mm_move(mm_move)
#provided.play_game(move_wrapper, 1, False)
poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)

#
# [EMPTY, EMPTY, PLAYERX]
# [EMPTY, EMPTY, EMPTY]
# [EMPTY, EMPTY, EMPTY],
# PLAYERO expected score 0 but received (-1, (1, 2))
#
# [PLAYERX, EMPTY, EMPTY]
# [PLAYERO, PLAYERO, EMPTY]
# [EMPTY, PLAYERX, EMPTY]
# PLAYERX returned bad move (1, (0, 2)
#
#
