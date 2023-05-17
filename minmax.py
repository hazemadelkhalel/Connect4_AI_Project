
from utility import *
from board import *

INF = 1000000000


def getBestMove(board, availableMoves, diff):
    alpha = -INF*10
    beta = INF*10
    bestScore = -INF*10
    move = -1

    for i in range(0, 7):
        if availableMoves[i] == 6:
            continue
        board = makeBoardMove(board, availableMoves[i], i, RED)
        availableMoves[i] += 1
        currentScore = MiniBeta(board, availableMoves, alpha, beta, diff)
        if currentScore > bestScore:
            bestScore = currentScore
            move = i
        availableMoves[i] -= 1
        unmakeBoardMove(board, availableMoves[i], i)
    return move

def MiniBeta(board, availableMoves, oldAlpha, oldBeta, diffculity):
    if gameIsOver(board) or canPlay(availableMoves) == False or diffculity == 0:
        return calculateOverAllScore(board)
    beta = oldBeta
    for i in range(0, 7):
        if availableMoves[i] == 6:
            continue
        bestScore = float("-inf")
        if oldAlpha < beta:
            board = makeBoardMove(board, availableMoves[i], i, BLUE)
            availableMoves[i] += 1
            bestScore = MaxAlpha(board, availableMoves, oldAlpha, beta, diffculity - 1)
            availableMoves[i] -= 1
            board = unmakeBoardMove(board, availableMoves[i], i)
        if bestScore < beta:
            beta = bestScore
    return beta

def MaxAlpha(board, availableMoves, oldAlpha, oldBeta, diffculity):
    if gameIsOver(board) or canPlay(availableMoves) == False or diffculity == 0:
        return calculateOverAllScore(board)
    alpha = oldAlpha
    for i in range(0, 7):
        if availableMoves[i] == 6:
            continue
        bestScore = float("-inf")
        if alpha < oldBeta:
            board = makeBoardMove(board, availableMoves[i], i, RED)
            availableMoves[i] += 1
            bestScore = MiniBeta(board, availableMoves, alpha, oldBeta, diffculity - 1)
            availableMoves[i] -= 1
            board = unmakeBoardMove(board, availableMoves[i], i)
        if bestScore > alpha:
            alpha = bestScore
    return alpha