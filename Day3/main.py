# AoC 2022 - Heme98
import Helpers.utils
import string

priority = string.ascii_lowercase + string.ascii_uppercase

def partOne(inputList, finalScore):
    for rucksack in inputList:
        common = set(rucksack[:len(rucksack)//2]) & set(rucksack[len(rucksack)//2:])
        finalScore += priority.index(common.pop()) + 1
    return finalScore

def partTwo(inputList, finalScore, increment):
    for i in range(0, len(inputList), increment):
        common = (set(inputList[i]) & set(inputList[i + 1]) & set(inputList[i + 2]))
        finalScore += priority.index(common.pop()) + 1
    return finalScore

if __name__ == '__main__':
    inputList = Helpers.utils.fileToList("input")
    Helpers.utils.debug2("Day 3, Part 1: ", partOne(inputList, 0))
    Helpers.utils.debug2("Day 3, Part 2: ", partTwo(inputList, 0, 3))