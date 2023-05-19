from utility import *
from board import *
def is_terminal_node(board):
    return winningMove(board, AGENT_PIECE) or winningMove(board, COMPUTER_PIECE) or len(getValidMoves(board)) == 0

def minimaxAlphaBeta(board, depth, alpha, beta, maximizingPlayer):
    validMoves = getValidMoves(board)
    is_over = is_terminal_node(board)
    if depth == 0 or is_over:
        if is_over:
            if winningMove(board, COMPUTER_PIECE):
                return (None, 100000000000000)
            elif winningMove(board, AGENT_PIECE):
                return (None, -10000000000000)
            else:  # Game is over, no more valid moves
                return (None, 0)
        else:  # Depth is zero
            return (None, scoreBoard(board, COMPUTER_PIECE))
    if maximizingPlayer:
        bestScore = -math.inf
        column = random.choice(validMoves)
        for col in validMoves:
            row = getNextValidRow(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, COMPUTER_PIECE)
            curScore = minimaxAlphaBeta(b_copy, depth - 1, alpha, beta, False)[1]
            if curScore > bestScore:
                bestScore = curScore
                column = col
            alpha = max(alpha, bestScore)
            if alpha >= beta:
                break
        return column, bestScore

    else:  # Minimizing player
        bestScore = math.inf
        column = random.choice(validMoves)
        for col in validMoves:
            row = getNextValidRow(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, AGENT_PIECE)
            curScore = minimaxAlphaBeta(b_copy, depth - 1, alpha, beta, True)[1]
            if curScore < bestScore:
                bestScore = curScore
                column = col
            beta = min(beta, bestScore)
            if alpha >= beta:
                break
        return column, bestScore




def minimax(board, depth, maximizingPlayer):
    validMoves = getValidMoves(board)
    is_over = is_terminal_node(board)
    if depth == 0 or is_over:
        if is_over:
            if winningMove(board, COMPUTER_PIECE):
                return (None, 100000000000000)
            elif winningMove(board, AGENT_PIECE):
                return (None, -10000000000000)
            else:  # Game is over, no more valid moves
                return (None, 0)
        else:  # Depth is zero
            return (None, scoreBoard(board, COMPUTER_PIECE))
    if maximizingPlayer:
        bestScore = -math.inf
        column = random.choice(validMoves)
        for col in validMoves:
            row = getNextValidRow(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, COMPUTER_PIECE)
            curScore = minimax(b_copy, depth - 1, False)[1]
            if curScore > bestScore:
                bestScore = curScore
                column = col
        return column, bestScore

    else:  # Minimizing player
        bestScore = math.inf
        column = random.choice(validMoves)
        for col in validMoves:
            row = getNextValidRow(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, AGENT_PIECE)
            curScore = minimax(b_copy, depth - 1, True)[1]
            if curScore < bestScore:
                bestScore = curScore
                column = col
        return column, bestScore
