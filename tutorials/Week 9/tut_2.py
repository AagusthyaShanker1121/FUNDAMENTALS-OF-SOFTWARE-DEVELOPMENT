# Step 1: The Player class - Java
# • Player has three fields:
# score (0 <= score <= 10) randomly generated
# index initialized from parameter [ Index must be incremental starting from 1. HINT: do this in the Game class ]
# • Player object information: Player_<index> score: <score>
# Step 2: The Game class - Java
# • Game has a list of players with a constructor that creates the list of players
# • Game has a method that initializes the list with 10 players
# • Game has the save() method save the players to a new file “game.data”, if previous game is saved, append the file
# • Game has the show() method that displays the game.data contents
# • Game has a menu method that offers the following choices (p/s/v/x)
# ( p ) play
# ( s ) save
# ( v ) show
# ( x ) exit
# • Game has a help method to show the choices and the read function to read the choices
# • Game has the main() method that invokes the system menu()
from random import randint
import json
import os

class Player:
    idx = 1
    def __init__(self, idx = None, score = None):
        self.score = randint(0, 10) if score == None else score
        self.idx = self.idx if idx == None else idx

    @classmethod
    def increment_idx(cls):
        cls.idx += 1

class Game:
    file_name = "game.data"

    def __init__(self):
        self.load()
        self.players = []
        
    def play(self, num_of_players):
        for i in range(num_of_players):
            self.players.append(Player())
            Player.increment_idx()
        print("\n")
        print(f"Player Scores: {[i.score for i in self.players]}")
        self.players_to_dict()
        print(f"Game loaded!\n")
        self.save()
    
    def players_to_dict(self):
        for i in range(len(self.players)):
            player_idx = self.players[i].idx
            player_score = self.players[i].score
            self.players_dict.update({player_idx: player_score})
        print(f"Players succesfully converted to dict: {self.players_dict}")
        return None

    def save(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'w+') as f:
                f.write(json.dumps(self.players_dict))
                print("Players saved succesfully.")
        else:
            with open(self.file_name, 'w') as f:
                f.write(json.dumps(self.players_dict))
                print("Players saved succesfully.")

    def load(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as f:
                self.players_dict = json.loads(f.read())
                print("Players loaded succesfully.")
        else:
            self.players_dict = {}
        for i in self.players_dict.keys():
            self.players.append(Player(i, ))
        return None

    def show(self):
        for i in range(len(self.players)):
            print(f"Player Index: {self.players[i].idx}. Score: {self.players[i].score}")
            print("\n")

class Menu:
    def __init__(self, game):
        self.menu()

    def get_input(self):
        x = input("Enter menu option (p/s/v/x)")
        return x

    def menu(self):
        curr_input = self.get_input()
        while curr_input != "x":
            match curr_input:
                case "p":
                    game.play(10)
                case "s":
                    game.save()
                case "v":
                    game.show()
            curr_input = self.get_input()

game = Game()
menu = Menu(game)
