"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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
    counter = 0

    for row in board:
        for item in row:
            if item is not None:
                counter += 1

    if counter % 2 == 0:
        return 'X'
    else:
        return 'O'


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_actions = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == None:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] is not None:
        raise Exception("Board cell already filled.")
    board_copy = deepcopy(board)
    board_copy[action[0]][action[1]] = player(board_copy)

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for row in board:
        if row[0] == row[1] == row[2]:
            if row[0] != None:
                return row[0]
            else:
                return None

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] != None:
                return board[0][i]
            else:
                return None

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] != None:
            return board[0][0]
        else:
            return None

    if board[2][0] == board[1][1] == board[0][2]:
        if board[2][0] != None:
            return board[2][0]
        else:
            return None

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    else:
        for row in board:
            for item in row:
                if item == None:
                    return False
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) and winner(board) == X:
        return 1
    elif winner(board) and winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    elif player(board) == X:
        possible_moves = []
        for action in actions(board):
            possible_moves.append((min_value(result(board, action)), action))
        #another way: 
        #sorted(possible_moves, key=lambda tup: tup[0], reverse=true)[1]
        return max(possible_moves, key=lambda tup: tup[0])[1]
    elif player(board) == O:
        possible_moves = []
        for action in actions(board):
            possible_moves.append((max_value(result(board, action)), action))
        #another way: 
        #sorted(possible_moves, key=lambda tup: tup[0])[1]
        return min(possible_moves, key= lambda tup: tup[0])[1]


def max_value(board):
    v = -math.inf;

    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v
    
def min_value(board):
    v = math.inf

    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v