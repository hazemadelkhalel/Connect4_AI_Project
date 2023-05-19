import numpy as np
import random
import pygame
import sys
import math
from utility import *
from minmax import *

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)



AGENT = 0
COMPUTER = 1

EMPTY = 0
AGENT_PIECE = 1
COMPUTER_PIECE = 2

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (
                int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == AGENT_PIECE:
                pygame.draw.circle(screen, RED, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == COMPUTER_PIECE:
                pygame.draw.circle(screen, YELLOW, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()


board = create_board()
print_board(board)
game_over = False

pygame.init()

SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE / 2.1 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 60)

turn = random.randint(AGENT, COMPUTER)

moves = 42
while not game_over and moves > 0:
    pygame.display.update()
    if turn == AGENT:
        col, minimax_score = minimaxAlphaBeta(board, 5, -math.inf, math.inf, True)

        if checkValidLocation(board, col):
            row = getNextValidRow(board, col)
            drop_piece(board, row, col, AGENT_PIECE)
            if winningMove(board, AGENT_PIECE):
                label = myfont.render("AGENT Red wins !", 1, RED)
                screen.blit(label, (40, 10))
                game_over = True
            print_board(board)
            draw_board(board)
            turn += 1
            turn = turn % 2

    # # Ask for AGENT 2 Input
    else:
        col, minimax_score = minimax(board, 3, True)
        if checkValidLocation(board, col):
            row = getNextValidRow(board, col)
            drop_piece(board, row, col, COMPUTER_PIECE)
            if winningMove(board, COMPUTER_PIECE):
                label = myfont.render("AGENT Yellow wins !", 1, YELLOW)
                screen.blit(label, (40, 10))
                game_over = True

            print_board(board)
            draw_board(board)
            turn += 1
            turn = turn % 2


    moves -= 1
    pygame.time.wait(500)
    if game_over:
        pygame.time.wait(6000)
if moves == 0:
    label = myfont.render("       Draw", 1, (255, 255, 255))
    screen.blit(label, (40, 10))
    pygame.display.update()
    pygame.time.wait(6000)