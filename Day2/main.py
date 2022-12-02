# AoC 2022 - Heme98
import Helpers.utils

class Rules:
    WIN = 6
    DRAW = 3
    choices = ["X", "Y", "Z"]

def calculateWinner(challenge, user):
    if (Rules.choices.index(challenge) + 1) == (Rules.choices.index(user) + 1):
        return Rules.DRAW
    elif ((Rules.choices.index(challenge) + 1) + 1) % 3 == (Rules.choices.index(user) + 1) % 3:
        return Rules.WIN
    return 0

def PartOne(inputList):
    finalScore = 0
    for pair in inputList:
        convertLetter = chr(ord(pair[0]) + 23) # Convert A, B, C to X, Y, Z
        finalScore += (Rules.choices.index(pair[1]) + 1) + calculateWinner(convertLetter, pair[1])
    return finalScore

def PartTwo(inputList):
    finalScore = 0
    for pair in inputList:
        convertLetter = chr(ord(pair[0]) + 23) # Convert A, B, C to X, Y, Z
        choice = Rules.choices[((Rules.choices.index(convertLetter) + 1) + (Rules.choices.index(pair[1]) + 1)) % 3]
        finalScore += (Rules.choices.index(choice) + 1) + calculateWinner(convertLetter, choice)
    return finalScore

if __name__ == '__main__':
    inputList = Helpers.utils.fileToListSplit("input", " ")
    Helpers.utils.debug2("Day 2, Part 1: ", PartOne(inputList))
    Helpers.utils.debug2("Day 2, Part 2: ", PartTwo(inputList))
