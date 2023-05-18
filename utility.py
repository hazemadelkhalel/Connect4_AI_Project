EMPTY = 0
RED = 1
BLUE = 2

def cntVer(board, i, j, player):
    count = 0
    tempI = i + 1
    while tempI < 6 and board[tempI][j] == player:
        tempI += 1
        count += 1
    tempI = i - 1
    while tempI >= 0 and board[tempI][j] == player:
        tempI -= 1
        count += 1
    return count
def countVerticalSeq(board, player, cnt):
    for i in range(0, 6):
        for j in range(0, 7):
            if board[i][j] == player:
                if cntVer(board, i, j, player) + 1 >= cnt:
                    return 1
    return 0


def cntHor(board, i, j, player):
    count = 0
    tempJ = j + 1
    while tempJ < 7 and board[i][tempJ] == player:
        tempJ += 1
        count += 1
    tempJ = j - 1
    while tempJ >= 0 and board[i][tempJ] == player:
        tempJ -= 1
        count += 1
    return count
def countHorizontalSeq(board, player, cnt):
    for i in range(0, 6):
        for j in range(0, 7):
            if board[i][j] == player:
                if cntHor(board, i, j, player) + 1 >= cnt:
                    return 1
    return 0

def cntDiag1(board, i, j, player):
    count = 0
    tempJ = j + 1
    tempI = i + 1
    while tempJ < 7 and tempI < 6 and board[tempI][tempJ] == player:
        tempJ += 1
        tempI += 1
        count += 1
    tempJ = j - 1
    tempI = i - 1
    while tempI >= 0 and tempJ >= 0 and board[tempI][tempJ] == player:
        tempJ -= 1
        tempI -= 1
        count += 1
    return count
def countDiagonalSeq1(board, player, cnt):
    for i in range(0, 6):
        for j in range(0, 7):
            if board[i][j] == player:
                if cntDiag1(board, i, j, player) + 1 >= cnt:
                    return 1
    return 0

def cntDiag2(board, i, j, player):
    count = 0
    tempJ = j + 1
    tempI = i - 1
    while tempJ < 7 and tempI >= 0 and board[tempI][tempJ] == player:
        tempJ += 1
        tempI -= 1
        count += 1
    tempJ = j - 1
    tempI = i + 1
    while tempI < 6 and tempJ >= 0 and board[tempI][tempJ] == player:
        tempJ -= 1
        tempI += 1
        count += 1
    return count
def countDiagonalSeq2(board, player, cnt):
    for i in range(0, 6):
        for j in range(0, 7):
            if board[i][j] == player:
                if cntDiag2(board, i, j, player) + 1 >= cnt:
                    return 1
    return 0
def checkWin(board, player):
    count = 0
    count += countHorizontalSeq(board, player, 4)
    count += countVerticalSeq(board, player, 4)
    count += countDiagonalSeq1(board, player, 4)
    count += countDiagonalSeq2(board, player, 4)
    return count

def checkLoseState(board, availableMoves, player):
    for i in range(0, 7):
        if availableMoves[i] == 6:
            continue
        count = 0
        cnt1 = cntVer(board, availableMoves[i], i, player)
        cnt2 = cntHor(board, availableMoves[i], i, player)
        cnt3 = cntDiag1(board, availableMoves[i], i, player)
        cnt4 = cntDiag2(board, availableMoves[i], i, player)
        count = max(count, cnt1)
        count = max(count, cnt2)
        count = max(count, cnt3)
        count = max(count, cnt4)
        if count == 3:
            return i
    return -1
def calculateWeight(board, player):
    count2 = countHorizontalSeq(board, player, 2)
    count2 += countVerticalSeq(board, player, 2)
    count2 += countDiagonalSeq1(board, player, 2)
    count2 += countDiagonalSeq2(board, player, 2)

    count3 = countHorizontalSeq(board, player, 3)
    count3 += countVerticalSeq(board, player, 3)
    count3 += countDiagonalSeq1(board, player, 3)
    count3 += countDiagonalSeq2(board, player, 3)

    count4 = countHorizontalSeq(board, player, 4)
    count4 += countVerticalSeq(board, player, 4)
    count4 += countDiagonalSeq1(board, player, 4)
    count4 += countDiagonalSeq2(board, player, 4)

    weight = count2 * 10 + count3 * 100 + count4 * 1000
    return weight


def calculateOverAllScore(board):
    return calculateWeight(board, RED) - calculateWeight(board, BLUE)

def canPlay(availableMoves):
    for i in range(0, 7):
        if availableMoves[i] != 6:
            return True
    return False
def gameIsOver(board):
    if checkWin(board, RED) > 0 or checkWin(board, BLUE) > 0:
        return True
    else:
        return False



