# AoC 2022 - Heme98
import Helpers.utils

class Rules:
    WIN = 6
    DRAW = 3
    map = {"A": 1, "B": 2, "C": 3,
           "X": 1, "Y": 2, "Z": 3}

    choices = ["X", "Y", "Z"]

def calculateWinner(challenge, user):
    if Rules.map[challenge] == Rules.map[user]:
        return Rules.DRAW
    elif (Rules.map[challenge] + 1) % 3 == Rules.map[user] % 3:
        return Rules.WIN
    return 0

def PartOne(inputList):
    finalScore = 0
    for pair in inputList:
        finalScore += Rules.map[pair[1]] + calculateWinner(pair[0], pair[1])
    return finalScore

def PartTwo(inputList):
    finalScore = 0
    for pair in inputList:
        choice = Rules.choices[(Rules.map[pair[0]] + Rules.map[pair[1]]) % 3]
        finalScore += Rules.map[choice] + calculateWinner(pair[0], choice)
    return finalScore

if __name__ == '__main__':
    inputList = Helpers.utils.fileToListSplit("input", " ")
    Helpers.utils.debug2("Day 2, Part 1: ", PartOne(inputList))
    Helpers.utils.debug2("Day 2, Part 2: ", PartTwo(inputList))
