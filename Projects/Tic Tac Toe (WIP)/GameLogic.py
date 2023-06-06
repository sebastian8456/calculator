# GameLogic.py
# Contains the game logic

from Board import Board
from Player import Player
import os

clear = lambda: os.system('cls')

class Game:
    def __init__(self):
        # Player markers
        self.player1 = Player().player
        self.player2 = Player().player
        # Game board
        self.board = Board().board


    def replay(self):
        play_again = input('Do you want to play tic tac toe? Y/N: ')

        if play_again.lower()[0] == 'y':
            clear()
            return True
        else:
            return False
    

    def full_board_check(self):
        for num in range (1,9):
            if self.space_check(num):
                return False
            

    def display_board(self):
        print(f'{self.board[1]}|{self.board[2]}|{self.board[3]}\n-----\n{self.board[4]}|{self.board[5]}|{self.board[6]}\n-----\n{self.board[7]}|{self.board[8]}|{self.board[9]}')

    
    def space_check(self, position):
        return self.board[position] == ' '
    

    def update_board(self, marker, position):
        self.board[position] = marker
        return self.board
    

    def win_check(self, marker):
        if marker == self.board[1] == self.board[2] == self.board[3] or marker == self.board[4] == self.board[5] == self.board[6] or marker == self.board[7] == self.board[8] == self.board[9] or marker == self.board[1] == self.board[5] == self.board[9] or marker == self.board[7] == self.board[5] == self.board[3] or marker == self.board[1] == self.board[4] == self.board[7] or marker == self.board[2] == self.board[5] == self.board[8] or marker == self.board[3] == self.board[6] == self.board[9]:
            return True
        return False
    

    def player_choice(self):
        position = 0
        
        while position not in range(1,10) or not self.space_check(position):
            position = int(input('Choose a position(1-9): '))
        return position


    def play(self):
        print('Welcome to Tic Tac Toe!')
        while True:
            # Reset the board
            clear()
            game_on = True
            turn = 'Player 1'
            while game_on:
                if turn == 'Player 1':
                    print(f'Player 1 is {self.player1}\nPlayer 2 is {self.player2}\n')
                    print("Player 1's turn.")
                    self.display_board()
                    # Redundant board
                    position = self.player_choice()
                    self.update_board(self.player1, position)
                    clear()

                    if self.win_check(self.player1):
                        self.display_board()
                        print('Player 1 has won!')
                        game_on = False
                    else:
                        if self.full_board_check():
                            self.display_board()
                            print('The game is a draw!')
                            break
                        else:
                            turn = 'Player 2'

                # Player 2's turn
                else:
                    print(f'Player 1 is {self.player1}\nPlayer 2 is {self.player2}\n')
                    print("Player 2's turn.")
                    self.display_board()
                    position = self.player_choice()
                    self.update_board(self.player2, position)
                    clear()

                    if self.win_check(self.player2):
                        self.display_board()
                        print('Player 2 has won!')
                        game_on = False
                    else:
                        if self.full_board_check():
                            self.display_board()
                            print('The game is a draw!')
                            break
                        else:
                            turn = 'Player 1'

            if not self.replay():
                break