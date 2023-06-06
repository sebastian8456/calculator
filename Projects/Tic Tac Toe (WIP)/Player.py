# Player.py
# Class to represent the human player

class Player:
    def __init__(self):
        self.player = self.player_input()

    def player_input(self):
        marker = ''
        while marker not in['X','O']:
            marker = input(f'Choose a marker X/O: ').upper()
        return marker
    