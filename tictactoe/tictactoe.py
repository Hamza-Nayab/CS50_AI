import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    rem = 0
    for line in board:
        rem += line.count(EMPTY)

    if rem % 2 == 0:
        return O
    return X


def actions(board):
    emp = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                emp.add((i, j))
    return emp


def result(board, action):
    if action not in actions(board):
        raise Exception("invalid")
    r, c = action
    cpy = copy.deepcopy(board)
    cpy[r][c] = player(board)
    return cpy


def Rowchk(board, player):
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    return False


def Colchk(board, player):
    for col in range(len(board[0])):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    return False


def chkdiag(board, player):
    count = 0
    count2 = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if row == col and board[row][col] == player:
                count += 1
            if (len(board) - row - 1) == col and board[row][col] == player:
                count2 += 1
    if count == 3 or count2 == 3:
        return True
    return False


def winner(board):
    if Rowchk(board, X) or Colchk(board, X) or chkdiag(board, X):
        return X
    elif Rowchk(board, O) or Colchk(board, O) or chkdiag(board, O):
        return O
    else:
        return None


def terminal(board):
    if winner(board) == X or winner(board) == O:
        return True
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == EMPTY:
                return False
    return True


def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def maxval(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, minval(result(board, action)))
    return v


def minval(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, maxval(result(board, action)))
    return v


def minimax(board):
    if terminal(board):
        return None
    elif player(board) == X:
        avail = []
        for action in actions(board):
            avail.append([minval(result(board, action)), action])
        return sorted(avail, key=lambda x: x[0], reverse=True)[0][1]
    elif player(board) == O:
        avail = []
        for action in actions(board):
            avail.append([maxval(result(board, action)), action])
        return sorted(avail, key=lambda x: x[0])[0][1]
