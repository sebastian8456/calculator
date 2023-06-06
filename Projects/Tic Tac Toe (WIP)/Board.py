# Board.py
# Represent the game board using tkinter
"""Create a gui for tic tac toe"""

from tkinter import *

class Board:

    def __init__(self):
        # Temporary
        self.board = [' '] * 10


board = Board()