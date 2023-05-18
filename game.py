from board import *
from minmax import *
import time
import random

# GAME LINK
# http://kevinshannon.com/connect4/
EMPTY = 0
RED = 1
BLUE = 2

def main():
    board = initBoard()
    print("Enter the difficulty: 1 To 5")
    diff = int(input())
    availableMoves = [0, 0, 0, 0, 0, 0, 0]
    Player = RED
    while not (gameIsOver(board)) and canPlay(availableMoves):
        if Player == RED:
            # Move by Agent
            BestMove = getBestMove(board, availableMoves, diff)
            board = makeBoardMove(board, availableMoves[BestMove], BestMove, RED)
            availableMoves[BestMove] += 1
            Player = BLUE
        else:
            # Move by AI
            random_column = 0
            while True:
                random_column = random.randint(0, 6)
                if availableMoves[random_column] != 6:
                    break
            board = makeBoardMove(board, availableMoves[random_column], random_column, BLUE)
            availableMoves[random_column] += 1
            Player = RED
        print_grid(board)
    if checkWin(board, RED) > 0:
        print("Player Red Wins\n")
    elif checkWin(board, BLUE) > 0:
        print("Player Blue Wins\n")
    else:
        print("Draw\n")

if __name__ == "__main__":
    main()
