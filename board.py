from PIL import ImageGrab
import pyautogui

# YOU MAY NEED TO CHANGE THESE VALUES BASED ON YOUR SCREEN SIZE
LEFT = 570
TOP = 200
RIGHT = 1350
BOTTOM = 875

EMPTY = 0
RED = 1
BLUE = 2

def initBoard():
    board = [[EMPTY for i in range(7)] for j in range(6)]
    return board
def print_grid(board):

    for i in range(len(board) - 1, -1, -1):
        for j in range(0, len(board[i])):
            if board[i][j] == EMPTY:
                print("*", end=" \t")
            elif board[i][j] == RED:
                print("R", end=" \t")
            elif board[i][j] == BLUE:
                print("B", end=" \t")
        print("\n")
    print("\n")

def move(self, i, j, player):
    self.board[i][j] = player

def makeBoardMove(board, i, j, player):
    if j < 0:
        pass
    else:
        board[i][j] = player
    return board

def unmakeBoardMove(board, i, j):
    if j < 0:
        pass
    else:
        board[i][j] = EMPTY
    return board



