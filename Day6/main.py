# AoC 2022 - Heme98
import Helpers.utils

def detectMarker(input, target):
    for i in range(len(input)):
        if len(set(input[i:i + target])) == target:
            return input.find("".join([input[i:i+target]])) + target

def partOne(input, range):
    return detectMarker(input, range)

def partTwo(input, range):
    return detectMarker(input, range)

if __name__ == '__main__':
    file = Helpers.utils.fileToString("input")
    Helpers.utils.debug2("Day 6, Part 1: ", partOne(file, 4))
    Helpers.utils.debug2("Day 6, Part 2: ", partTwo(file, 14))
