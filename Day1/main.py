# AoC 2022 - Heme98
import Helpers.utils

# return a sorted list with all elves total calories
def sumAllGroups(inputList):
    totalCalories = [0]
    for calories in inputList:
        if calories == "":
            totalCalories.append(0)
            continue
        totalCalories[-1] += int(calories)
    return sorted(totalCalories)

# Part 1: get the elf with highest number of calories (last in list or use max())
def maxCalories(inputList):
    return sumAllGroups(inputList)[-1]

# Part 2: get top 3 elves with highest number of calories (last 3 in list) and sum the value
def top3MaxCalories(inputList, target):
    return sum(sumAllGroups(inputList)[-target:])

if __name__ == '__main__':
    inputList = Helpers.utils.fileToListStrip("input")
    Helpers.utils.debug2("Day 1, Part 1: ", maxCalories(inputList))
    Helpers.utils.debug2("Day 1, Part 2: ", top3MaxCalories(inputList, 3))
