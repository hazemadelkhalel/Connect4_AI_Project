import numpy as np
import tkinter as tk
import GUIgame
from tkinter import messagebox

# Constants

# Global variables
difficulty = 5
algorithm = 0


def start_game():
    global difficulty
    global algorithm
    difficulty = int(difficulty_var.get())
    if Choose_algorithm.get() == "Random":
        algorithm = 0
    else:
        algorithm = 1

    difficulty_window.destroy()
    play_game()


def play_game():
    print("%d"%algorithm)
    GUIgame.GUIGame(difficulty, algorithm)


# Create difficulty selection GUI
difficulty_window = tk.Tk()
difficulty_window.title("Connect Four - Difficulty")
difficulty_window.geometry("600x400")

difficulty_label = tk.Label(difficulty_window, text="Select Difficulty")
difficulty_label.pack(pady=10)

difficulty_var = tk.StringVar()
difficulty_var.set("5")

difficulty_options = ["1", "2", "3", "4", "5"]
difficulty_dropdown = tk.OptionMenu(difficulty_window, difficulty_var, *difficulty_options)
difficulty_dropdown.pack(pady=5)

Choose_algorithm = tk.Label(difficulty_window, text="Choose algorithm")
Choose_algorithm.pack(pady=10)

Choose_algorithm = tk.StringVar()
Choose_algorithm.set("Random")

algorithm_options = ["Random", "MiniMax"]
algorithm_dropdown = tk.OptionMenu(difficulty_window, Choose_algorithm, *algorithm_options)
algorithm_dropdown.pack(pady=5)

start_button = tk.Button(difficulty_window, text="Start Game", command=start_game)
start_button.pack(pady=10)
difficulty_window.mainloop()
