# AoC 2022 - Heme98
import Helpers.utils

choices = ["X", "Y", "Z"]

def calculateWinner(challenge, user):
    if (choices.index(challenge)) == (choices.index(user)):
        return 3
    elif ((choices.index(challenge)) + 1) % 3 == (choices.index(user)) % 3:
        return 6
    return 0

def PartOne(inputList, finalScore):
    for pair in inputList:
        convertLetter = chr(ord(pair[0]) + 23) # Convert A, B, C to X, Y, Z
        finalScore += (choices.index(pair[1]) + 1) + calculateWinner(convertLetter, pair[1])
    return finalScore

def PartTwo(inputList, finalScore):
    for pair in inputList:
        convertLetter = chr(ord(pair[0]) + 23) # Convert A, B, C to X, Y, Z
        choice = choices[((choices.index(convertLetter) + 1) + (choices.index(pair[1]) + 1)) % 3]
        finalScore += (choices.index(choice) + 1) + calculateWinner(convertLetter, choice)
    return finalScore

if __name__ == '__main__':
    inputList = Helpers.utils.fileToListSplit("input.txt", " ")
    Helpers.utils.debug2("Day 2, Part 1: ", PartOne(inputList, 0))
    Helpers.utils.debug2("Day 2, Part 2: ", PartTwo(inputList, 0))
