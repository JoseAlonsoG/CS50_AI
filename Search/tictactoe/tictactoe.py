"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # raise NotImplementedError
    X_value = 0
    O_value = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X":
                X_value += 1
            elif board[i][j] == "O":
                O_value += 1
            else:
                pass
    if X_value == 0:
        return X
    elif (X_value + O_value) % 2 != 0:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # raise NotImplementedError
    set_actions = set()
    for i in range(3):
        for j in range(3):
            # if ((board[i][j] != X) or (board[i][j] != O)):
            if (board[i][j] == EMPTY):
                set_actions.add((i,j))
            else:
                pass
    return set_actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # raise NotImplementedError
    f_board = copy.deepcopy(board)
    who_play = player(board)
    i, j = action

    if board[i][j] != None:
        raise Exception
        
    if who_play == 'X':
        f_board[i][j] = X
    else:
        f_board[i][j] = O

    return f_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # raise NotImplementedError
    for i in range(3):
        if board[i].count(X) == 3:
            return X
        elif board[i].count(O) == 3:
            return O
    for j in range(3):
        column = []
        for i in range(3):
            column.append(board[i][j])
        if column.count(X) == 3:
            return X
        elif column.count(O) == 3:
            return O
        else:
            del column
    diagonal = []
    for i in range(3):
        diagonal.append(board[i][i])
    if diagonal.count(X) == 3:
        return X
    elif diagonal.count(O) == 3:
        return O
    else:
        del diagonal
    
    diagonal_neg = [board[2][0], board[1][1], board[0][2]]
    if diagonal_neg.count(X) == 3:
        return X
    elif diagonal_neg.count(O) == 3:
        return O
    else:
        del diagonal_neg

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # raise NotImplementedError
    # game is won by one of the players
    if winner(board) != None:
        return True

    # there is possible moves
    for row in board:
        if EMPTY in row:
            return False
    
    # no possible moves left
    return True
    # return False if utility(board) == 0 else True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # raise NotImplementedError
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # raise NotImplementedError
    curr_player = player(board)

    if terminal(board):
        return None

    if curr_player == X:
        return max_value(board)[1]

    else:
        return min_value(board)[1]


def max_value(board):
    """XXX"""
    optimal_action = ()
    if terminal(board):
        return utility(board), optimal_action
    else:
        v = - math.inf
        for action in actions(board):
            v_opt = max(v, min_value(result(board, action))[0])
            if v_opt > v:
                v = v_opt
                optimal_action = action
        return v, optimal_action

def min_value(board):
    """XXX"""
    optimal_action = ()
    if terminal(board):
        return utility(board), optimal_action
    else:
        v = math.inf
        for action in actions(board):
            v_opt = min(v, max_value(result(board, action))[0])
            if v_opt < v:
                v = v_opt
                optimal_action = action
        return v, optimal_action
