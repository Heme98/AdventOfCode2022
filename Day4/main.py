# AoC 2022 - Heme98
import Helpers.utils

def getSets(pair):
    ranges = list(map(int, pair.replace(",", "-").split("-")))
    return set(range(ranges[0], ranges[1]+1)), set(range(ranges[2], ranges[3]+1))

def partOne(inputList, finalScore):
    for pair in inputList:
        setA, setB = getSets(pair)
        if setA.issubset(setB) or setB.issubset(setA):
            finalScore += 1
    return finalScore

def partTwo(inputList, finalScore):
    for pair in inputList:
        setA, setB = getSets(pair)
        if setA & setB:
            finalScore += 1
    return finalScore

if __name__ == '__main__':
    inputList = Helpers.utils.fileToListStrip("input.txt")
    Helpers.utils.debug2("Day 4, Part 1: ", partOne(inputList, 0))
    Helpers.utils.debug2("Day 4, Part 2: ", partTwo(inputList, 0))