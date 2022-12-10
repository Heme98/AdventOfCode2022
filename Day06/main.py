# AoC 2022 - Heme98
import Helpers.utils

def partOne(input, target):
    return [i + target for i in range(len(input)) if len(set(input[i:i + target])) == target][0]

def partTwo(input, target):
    return [i + target for i in range(len(input)) if len(set(input[i:i + target])) == target][0]

if __name__ == '__main__':
    file = Helpers.utils.fileToString("input.txt")
    Helpers.utils.debug2("Day 6, Part 1: ", partOne(file, 4))
    Helpers.utils.debug2("Day 6, Part 2: ", partTwo(file, 14))