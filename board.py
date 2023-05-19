import numpy as np
import random
import pygame
import sys
import math
from utility import *


ROW_COUNT = 6
COLUMN_COUNT = 7
def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def checkValidLocation(board, col):
    return board[ROW_COUNT - 1][col] == 0


def getNextValidRow(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(np.flip(board, 0))

