#!/usr/bin/env python3
#CHECKLIST
#   #1 done
#   #2 Done\
#   #3 DONE 
#   #4 DONE
#   #5 Reflect part done
#   #5 DONE
#   #6 Already done and typos solved
#   #7 Done


import string
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']
types = ['random', 'reflect','cycle']
count = 0
"""The Player class is the parent class for all of the Players
in this game"""
class Player:
    
    def __init__(self, name):
        self.name = name
        self.my_move = None
        self.their_move = None
    def move(self):
        #must ask user for the move and return it
        #HERE WHY WE WEILL IMPORT TWO
        #ONE HUMAN PLAYER AND ONE COMPUTER
        # THE COMPUTER SUBCLASS WILL DEPEND ON LEARN METHOD
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    def beats(self, one, two):
    #This shouldnt change at all
        return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

#------------------------------------------------------------------------
# ------ First class is for the Robot------------------------------
class RandomPlayer (Player) :
    def move(self):
        return random.choice(moves)

#---------Second class is for the Robot----------------------------
class ReflectPlayer (Player) :

    def move(self):
        
        now_move = self.their_move
        if now_move == None:
            now_move = random.choice(moves)
            return now_move
        else:
            return now_move  

#---------- Third class is for the Robot-----------------------------
class CyclePlayer (Player):
    def move(self): 
        last_move = self.my_move
        if last_move == None:
            last_move = random.choice(moves)
            return last_move
        index = moves.index(last_move)
        if index == (len(moves)-1):
            index = 0
            return moves[index]
        else:
            new_move = moves[index+1]
            return new_move

#-----------------------------------------------------------------------
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
        self.round_numbers = 0
        self.human_wins = 0
        self.robot_wins = 0
        self.winner = None

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
        while True:
            print("--------------------------------------------")
            print(f"Round {round}:\n")
            self.play_round()
            #CHECK SELF.LEARN AND DO THE SAME
            if self.p1.beats(self.move1, self.move2):
                print(f"!! Player {self.p1.name} Won !! \n")
                self.human_wins += 1
                if self.human_wins == 3:
                    self.winner = self.p1.name
                    break

            elif self.p2.beats(self.move2, self.move1):
                print(f"Player {self.p2.name} Won \n")
                self.robot_wins += 1
                if self.robot_wins ==3:
                    self.winner = self.p2.name
                    break
            else:
                print("It is a tie\n")

# self.p1 beats self.p2.
        print("---------------------------------------------------\n")
        print("---------------------------------------------------\n")
        print("Game over!\n")
        print(f"{self.p1.name} scored {self.human_wins}\t ||\t {self.p2.name} scored {self.robot_wins} \n")
        print(f"*****Congratz {self.winner}*****\n")


if __name__ == '__main__':
    types = ['random', 'reflect','cycle']
    while True:
        game_type = input("What type of game mode? random, reflect or cycle?\n")
        if game_type == types[0].lower():
            game = Game(HumanPlayer("Human"), RandomPlayer("Random-Robot"))
            game.play_game()
            break

        elif game_type == types[1].lower():
            game = Game(HumanPlayer("Human"), ReflectPlayer("Reflect-Robot"))
            game.play_game()
            break

        elif game_type == types[2].lower():
            game = Game(HumanPlayer("Human"), CyclePlayer("Cycle-Robot"))
            game.play_game()
            break
        else:
            print("You entered wrong robot name\n")