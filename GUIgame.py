
import numpy as np
import random
import pygame
import sys
from minmax import *
import math
BLUE = (0, 0, 255)
BLACK = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ROW_COUNT = 6
COLUMN_COUNT = 7

PLAYER = 0
AI = 1

EMPTY = 0
PLAYER_PIECE = 1
AI_PIECE = 2

WINDOW_LENGTH = 4

def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def print_board(board):
    print(np.flip(board, 0))

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (
            int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == PLAYER_PIECE:
                pygame.draw.circle(screen, RED, (
                int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == AI_PIECE:
                pygame.draw.circle(screen, YELLOW, (
                int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()


def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True

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

myfont = pygame.font.SysFont("monospace", 75)

turn = random.randint(PLAYER, AI)


boardH = initBoard()
print("Enter the difficulty: 1 To 5")
diff = int(input())
availableMoves = [0, 0, 0, 0, 0, 0, 0]
Player = RED
# while not (gameIsOver(boardH)) and canPlay(availableMoves):
#     if Player == RED:
#         # Move by Agent
#         BestMove = getBestMove(boardH, availableMoves, diff)
#         boardH = makeBoardMove(boardH, availableMoves[BestMove], BestMove, RED)
#         availableMoves[BestMove] += 1
#         Player = BLUE
#     else:
#         # Move by AI
#         random_column = 0
#         while True:
#             random_column = random.randint(0, 6)
#             if availableMoves[random_column] != 6:
#                 break
#         boardH = makeBoardMove(boardH, availableMoves[random_column], random_column, BLUE)
#         availableMoves[random_column] += 1
#         Player = RED



while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # if event.type == pygame.MOUSEMOTION:
        #     pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
        #     posx = event.pos[0]
        #     if turn == PLAYER:
        #         pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)

        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            # print(event.pos)
            # Ask for Player 1 Input
            if turn == PLAYER:
                BestMove = getBestMove(boardH, availableMoves, diff)
                boardH = makeBoardMove(boardH, availableMoves[BestMove], BestMove, RED)
                # posx = event.pos[0]
                posx = availableMoves[BestMove]
                col = BestMove
                availableMoves[BestMove] += 1

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, PLAYER_PIECE)

                    if winning_move(board, PLAYER_PIECE):
                        label = myfont.render("Player 1 wins!!", 1, RED)
                        screen.blit(label, (40, 10))
                        game_over = True

                    turn += 1
                    turn = turn % 2

                    print_board(board)
                    draw_board(board)

    # # Ask for Player 2 Input
    if turn == AI and not game_over:

        # col = random.randint(0, COLUMN_COUNT-1)
        # col = pick_best_move(board, AI_PIECE)
        random_column = 0
        while True:
            random_column = random.randint(0, 6)
            if availableMoves[random_column] != 6:
                break
        boardH = makeBoardMove(boardH, availableMoves[random_column], random_column, BLUE)
        col, minimax_score = random_column,availableMoves[random_column]
        availableMoves[random_column] += 1

        if is_valid_location(board, col):
            # pygame.time.wait(500)
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, AI_PIECE)

            if winning_move(board, AI_PIECE):
                label = myfont.render("Player 2 wins!!", 1, YELLOW)
                screen.blit(label, (40, 10))
                game_over = True

            print_board(board)
            draw_board(board)

            turn += 1
            turn = turn % 2

    if game_over:
        pygame.time.wait(3000)