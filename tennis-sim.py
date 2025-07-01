# tennis-sim.py

# Programmed by: W. Cale Morrison
from random import random

class Player:
    # Player keeps track of service probability and score
    def __init__(self, probability):
        # Create a player with this probability
        self.probability = probability
        self.score = 0

    def winsServe(self):
        # Returns a Boolean that is true with probability self.probability
        return random() < self.probability

    def incrementScore(self):
        # Add a point to this player's score
        self.score += 1

    def getScore(self):
        # Returns this player's current score
        return self.score


class TennisGame:
    # A TennisGame represent a game in progress. A game has two players
    # and keepts track of which one is currently serving
    def __init__(self, probabilityA, probabilityB):
        # Create a new game having players with given probabilities
        self.playerA = Player(probabilityA)
        self.playerB = Player(probabilityB)
        self.server = self.playerA # Player A always serves first

    def play(self):
        # Play the game to completion
        while not self.isOver():
            if self.server.winsServe():
                self.server.incrementScore()
            else:
                self.changeServer()

    def isOver(self):
        # Returns game is finished
        playerA_score, playerB_score = self.getScores()
        return playerA_score == 15 or playerB_score == 15 or \
    (playerA_score == 7 and playerB_score == 0) or (playerA_score == 0 and playerB_score == 7)

    def changeServer(self):
        # Switch which player is serving
        if self.server == self.playerA:
            self.server = self.playerB
        else:
            self.server = self.playerA

    def getScores(self):
        # Returns the current scores of player A and player B
        return self.playerA.getScore(), self.playerB.getScore()


class SimulationStatistics:
    # SimulationStatistics handsles accumulation of statistics across multiple
    # completed games. This also tracks the wins and shutouts for each player
    def __init__(self):
        # Create a new accumulator for a series of games
        self.winsA = 0
        self.winsB = 0
        self.shutoutsA = 0
        self.shutoutsB = 0

    def update(self, game):
        # Determine the outcome of a game and update statistics
        playerA_score, playerB_score = game.getScores()
        if playerA_score > playerB_score: # Player A won the game
            self.winsA += 1
            if playerB_score == 0:
                self.shutoutsA += 1
        else: # Player B won the game
            self.winsB += 1
            if playerA_score == 0:
                self.shutoutsB += 1

    def printReport(self):
        # Print a nicely formatted report
        total_wins = self.winsA + self.winsB
        print("\nSummary of ", total_wins, " games:\n")
        print("         wins (% total)    shutouts (% wins)     ")
        print("-------------------------------------------------")
        self.printLine("A", self.winsA, self.shutoutsA, total_wins)
        self.printLine("B", self.winsB, self.shutoutsB, total_wins)

    def printLine(self, label, wins, shutouts, total_games):
        template = "Player {0}:{1:5} ({2:5.1%}) {3:11} ({4})"
        if wins == 0: # Avoid division by zero
            shutouts_string = "-----"
        else:
            shutouts_string = "{0:4.1%}".format(float(shutouts)/wins)
        print(template.format(label, wins, float(wins)/total_games, shutouts, shutouts_string))
        

def printIntro():
    print("This program simulates a game of tennis between two")
    print("players called 'A' and 'B'. The ability of each player is")
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.\n")

def getInputs():
    # Returns the three simulation parameters
    playerA = float(input("What is the probability player A wins a serve? "))
    playerB = float(input("What is the probability player B wins a serve? "))
    number_of_games = int(input("How many games to simulate? "))
    
    return playerA, playerB, number_of_games


def main():
    printIntro()

    probabilityA, probabilityB, number_of_games = getInputs()

    # Play the games
    stats = SimulationStatistics()
    for i in range(number_of_games):
        the_game = TennisGame(probabilityA, probabilityB) # Create a new game
        the_game.play() # Play the game
        stats.update(the_game) # Extract game information

    # Print the results
    stats.printReport()
    input("\nPress <Enter> to quit\n")

main()

    
