# AoC 2022 - Heme98
import Helpers.parser


# return a sorted list with all elves total calories
def sumAllGroups(inputList):
    totalCalories = []
    currentCalories = 0
    for calories in inputList:
        if calories == "":
            totalCalories.append(currentCalories)
            currentCalories = 0
        else:
            currentCalories += int(calories)
    return sorted(totalCalories)


# Part 1: get the elf with highest number of calories (last in list or use max())
def maxCalories(inputList):
    return sumAllGroups(inputList)[-1]


# Part 2: get top 3 elves with highest number of calories (last 3 in list) and sum the value
def top3MaxCalories(inputList, target):
    return sum(sumAllGroups(inputList)[-target:])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    inputList = Helpers.parser.fileToList("input")
    Helpers.parser.debug(maxCalories(inputList))
    Helpers.parser.debug(top3MaxCalories(inputList, 3))
