"""
Tic Tac Toe Player
"""

import math
import util
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
    xCounter = 0
    oCounter = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                xCounter += 1
            elif board[i][j] == O:
                oCounter += 1

    if terminal(board):
        return None

    if xCounter > oCounter:
        return O
    else:
        return X

    raise PlayerFunctionError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = set()
    if winner(board) is None:
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    possibleActions.add((i, j))
    return possibleActions
    raise ActionsFunctionError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    possibleActions = actions(board)
    if action not in possibleActions:
        raise Exception
    if action == None:
        return board
    if terminal(board):
        return board
    else:
        newBoard = copy.deepcopy(board)
        newBoard[action[0]][action[1]] = player(board)

    return newBoard

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for x in range(3):
        xCounter = 0
        oCounter = 0
        for i in range(3):
            if board[x][i] == X:
                xCounter += 1
            if board[x][i] == O:
                oCounter += 1
            if xCounter == 3:
                return X
            if oCounter == 3:
                return O

    for x in range(3):
        xCounter = 0
        oCounter = 0
        for i in range(3):
            if board[i][x] == X:
                xCounter += 1
            if board[i][x] == O:
                oCounter += 1
            if xCounter == 3:
                return X
            if oCounter == 3:
                return O

    xCounter = 0
    oCounter = 0
    for x in range(3):
        if board[x][x] == X:
            xCounter += 1
        if board[x][x] == O:
            oCounter += 1

        if xCounter == 3:
            return X
        if oCounter == 3:
            return O

    if board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X
    elif board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O

    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if len(actions(board)) == 0:
        return True

    return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    raise NotImplementedError


def minimax(board):
    results = minimaxSupport(board)

    return results[1]


def minimaxSupport(board):

    if terminal(board):
        return (utility(board), None)


# Maximizing player

    def maxi(board):
        value = [-1, None]
        bestAction = None
        if terminal(board):
            return utility(board), None
        for action in actions(board):
            lastValue = copy.deepcopy(value)
            mini_result = mini(result(board, action))
            value[0] = max(value[0], mini_result[0])
            if value[0] > lastValue[0]:
                bestAction = action
        return [value[0], bestAction]
        raise NotImplementedError
# Minimizing player

    def mini(board):
        value = [1, None]
        bestAction = None
        if terminal(board):
            return utility(board), None
        for action in actions(board):
            lastValue = copy.deepcopy(value)
            maxi_result = maxi(result(board, action))
            value[0] = min(value[0], maxi_result[0])
            if value[0] < lastValue[0]:
                bestAction = action
        return [value[0], bestAction]
        raise NotImplementedError

    if player(board) == X:
        results = maxi(board)
    elif player(board) == O:
        results = mini(board)

    return results
    raise NotImplementedError
