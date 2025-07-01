# volleyball-sim.py

# Programmed by: W. Cale Morrison
from random import random

def printIntro():
    print("This program simulates a game of volleyball between two")
    print("teams called 'A' and 'B'. The ability of each team is")
    print("indicated by a probability (a number between 0 and 1) that")
    print("the team wins the point when serving. Team A always")
    print("has the first serve.\n")

def getInputs():
    # Returns the three simulation parameters
    playerA = float(input("What is the probability team A wins a serve? "))
    playerB = float(input("What is the probability team B wins a serve? "))
    number_of_games = int(input("How many games to simulate? "))
    
    return playerA, playerB, number_of_games

def simulateNGames(number_of_games, probabilityA, probabilityB):
    # Simulates number_of_games of volleyball between teams whose
    #     abilities are represented by the probability of winning a serve
    # Returns the number of wins for A and B
    winsA = winsB = 0
    for i in range(number_of_games):
        scoreA, scoreB = simulateOneGame(probabilityA, probabilityB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simulateOneGame(probabilityA, probabilityB):
    # Simulates one game of tennis between players whose
    #     abilities are represented by the probability of winning a serve
    # Returns the number of wins for A and B
    serving = 'A'
    scoreA = 0
    scoreB = 0

    while not gameOver(scoreA, scoreB):
        if serving == 'A':
            if random() < probabilityA:
                scoreA += 1
            else:
                serving = 'B'
        else:
            if random() < probabilityB:
                scoreB = scoreB + 1
            else:
                serving = 'A'
    return scoreA, scoreB

def gameOver(scoreA, scoreB):
    # scoreA and scoreB represent scores for a volleyball game
    # Returns True if the game is over, False otherwise
    return scoreA == 15 or scoreB == 15

def printSummary(winsA, winsB):
    # Prints a summary of wins for each team
    total_wins = winsA + winsB
    print("\nGames simulated: ", total_wins)
    print("Wins for player A: {0} ({1:0.1%})".format(winsA, winsA/total_wins))
    print("Wins for player B: {0} ({1:0.1%})".format(winsB, winsB/total_wins))

def main():
    printIntro()
    probabilityA, probabilityB, number_of_games = getInputs()
    winsA, winsB = simulateNGames(number_of_games, probabilityA, probabilityB)
    printSummary(winsA, winsB)

main()
    
