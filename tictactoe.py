"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
point = {X: 1, O: -1, EMPTY: 0}
max_deep = 15

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
    emptyCounter = 0
    for row in range(3):
        for collum in range(3):
            if board[row][collum] == EMPTY:
                emptyCounter += 1
    return X if emptyCounter % 2 == 1 else O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for row in range(3):
        for collum in range(3):
            if board[row][collum] == EMPTY:
                moves.add((row,collum))
    return moves

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise Exception("Not validable move")
    newBoard = copy.deepcopy(board)
    newBoard[action[0]][action[0]] = player(board)
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    win = None
    for i in range(3):
        if board[i][i]:
            l = board[i]
            win = check_winner(l)
            if win: return win
            l = [board[0][i], board[1][i], board[2][i]]
            win = check_winner(l)
            if win: return win
    l = [board[0][0], board[1][1], board[2][2]]
    win = check_winner(l)
    if win: return win
    l = [board[0][2], board[1][1], board[2][0]]
    win = check_winner(l)
    if win: return win
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board): return True
    if actions(board): return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    return point[winner(board)]


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    p = player(board)
    if p == X:
        value, move = max_value(board,0)
    else:
        value, move = min_value(board,0)
    return move
    
def check_winner(line):
    if line[0] == line[1] and line[0] == line[2]:
        return line[0]
    return None

def max_value(board, step):
    if terminal(board) or step > max_deep:
        return utility(board), None
    value = -math.inf
    optimal_move = None
    for action in actions(board):
        v, move = value, min_value(result(board, action), step+1)
        if value < v:
            value = v
            optimal_move = action
            if value == 1:
                break
    return value, optimal_move

def min_value(board, step):
    if terminal(board) or step > max_deep:
        return utility(board), None
    value = math.inf
    optimal_move = None
    for action in actions(board):
        v, move = value, max_value(result(board, action), step+1)
        if value > v:
            value = v
            optimal_move = action
            if value == -1:
                break
    return value, optimal_move