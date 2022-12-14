# AoC 2022 - Heme98
import Helpers.utils

def buildCave(file, max_x, max_y):
    cave = [["."] * (max_x+1) for _ in range(max_y + 1)] # Create empty cave
    for item in file:
        previousPair = None
        for pair in item:
            if previousPair is not None:
                if int(previousPair[0]) < int(pair[0]):
                    for i in range(int(previousPair[0]), int(pair[0])+1):
                        cave[int(previousPair[1])][i] = "#"
                elif int(previousPair[0]) > int(pair[0]):
                    for i in range(int(pair[0]), int(previousPair[0])+1):
                        cave[int(previousPair[1])][i] = "#"
                if int(previousPair[1]) < int(pair[1]):
                    for i in range(int(previousPair[1]), int(pair[1])+1):
                        cave[i][int(previousPair[0])] = "#"
                elif int(previousPair[1]) > int(pair[1]):
                    for i in range(int(pair[1]), int(previousPair[1])+1):
                        cave[i][int(previousPair[0])] = "#"
            previousPair = pair
    return cave

def fillSand(cave, part1, count = 0):
    sandCoord = [0, 500]
    current = sandCoord
    condition = current[0] < len(cave)-1 if part1 else cave[current[0]][current[1]] != "o"
    while condition:
        if cave[current[0] + 1][current[1]] == ".":
            current = [current[0] + 1, current[1]]
        elif cave[current[0] + 1][current[1] - 1] == ".":
            current = [current[0] + 1, current[1] - 1]
        elif cave[current[0] + 1][current[1] + 1] == ".":
            current = [current[0] + 1, current[1] + 1]
        else:
            cave[current[0]][current[1]] = "o"
            count += 1
            current = sandCoord
        condition = current[0] < len(cave) - 1 if part1 else cave[current[0]][current[1]] != "o"
    return count

def partOne(file, max_x, max_y):
    cave = buildCave(file,max_x, max_y)
    return fillSand(cave, True)

def partTwo(file, max_x, max_y):
    cave = buildCave(file, max_x*2, max_y)
    cave.append(["."] * (max_x*2+1))  # Create space (multiple width of 2 to simulate infinity)
    cave.append(["#"] * (max_x*2 + 1))  # Create bottom (multiple width of 2 to simulate infinity)
    return fillSand(cave, False)

if __name__ == '__main__':
    file = Helpers.utils.fileToListSplit("input.txt", " -> ")
    file = [[x.split(",") for x in pair] for pair in file]
    max_y = int(max([max([int(y) for _, y in pair]) for pair in file]))
    max_x = int(max([max([int(x) for x, _ in pair]) for pair in file]))
    Helpers.utils.debug2("Day 14, Part 1: ", partOne(file, max_x, max_y))
    Helpers.utils.debug2("Day 14, Part 2: ", partTwo(file, max_x, max_y))
