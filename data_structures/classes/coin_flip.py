import random
import re

class Coin:
    def __init__(self, player_1, player_2):
        self.side = random.choice(["heads", "tails"])
        self.player_1 = player_1
        self.player_2 = player_2


    def get_player_1(self):
        return self.player_1

    def get_side(self):
        return self.side

    def get_player_2(self):
        return self.player_2



if __name__ == "__main__":

    # Prompt user for input
    player_1 = input("Enter player 1 name: ")
    player_2 = input("Enter player 2 name: ")



