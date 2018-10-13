#!/usr/bin/env python3
#CHECKLIST
#   #1 done
#   #2 Done\
#   #3 DONE 



import string
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    
    def __init__(self, name):
        self.name = name

    def move(self):
        #must ask user for the move and return it
        #HERE WHY WE WEILL IMPORT TWO
        #ONE HUMAN PLAYER AND ONE COMPUTER
        # THE COMPUTER SUBCLASS WILL DEPEND ON LEARN METHOD
        return 'rock'

    def learn(self, my_move, their_move):
        # We will use this bcz we will need a comupter subclass
        #It will use this to determine its next move
        #
        pass


    def beats(self, one, two):
    #This shouldnt change at all
        return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

#------------------------------------------------------------------------
class RandomPlayer (Player) :
    def move(self):
        return random.choice(moves)
#-----------------------------------------------------------------------
class HumanPlayer (Player):
    def move(self):
        while True:
            
            human_move = input(f"Please pick {moves[0]}, {moves[1]} or {moves[2]} \t")
            cr_human_move = human_move.lower()
            if cr_human_move in moves:
                return cr_human_move
                break
            else:
                print("\n-->> please type a correct move\n")
#-----------------------------------------------------------------------
class Game:
    def __init__(self, p1, p2):
        #It import two player, dunno why
        #This one too
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        #To keep score of first player
        self.move1 = move1
        move2 = self.p2.move()
        #To keep score of second player
        self.move2 = move2
        #Print players

        print(f" \n-->> {self.p1.name}: {move1} ||  {self.p2.name}: {move2}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)


    def play_game(self):
        print("Game start!")
        #NOT ROUD 3, should maybe need a list whatever
        for round in range(3):
            print("--------------------------------------------")
            print(f"Round {round}:\n")
            self.play_round()
            #CHECK SELF.LEARN AND DO THE SAME
            if self.p1.beats(self.move1, self.move2):
                print(f"!! Player {self.p1.name} Won !! \n")

            elif self.p2.beats(self.move2, self.move1):
                print(f"Player {self.p2.name} Won \n")
            else:
                print("It is a tie\n")

# self.p1 beats self.p2.
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer("Human"), RandomPlayer("Robot"))
    game.play_game()
