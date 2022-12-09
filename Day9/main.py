# AoC 2022 - Heme98
import Helpers.utils

visited = []

def istouchinghorizont(tail, head):
    return True if abs(tail[0] -head[0]) == 0 else abs(tail[0] - head[0]) == 1

def istouchingvert(tail, head):
    return True if abs(tail[1] -head[1]) == 0 else abs(tail[1] - head[1]) == 1

def step(tail, head, direction, amount):
    for _ in range(int(amount)):
        if direction == "R":
            head[0] += 1
            if (tail[1] == head[1]):
                if(not istouchinghorizont(tail, head)):
                    tail[0] += 1
            elif (not istouchinghorizont(tail, head)):
                tail[0] += 1
                tail[1] = head[1]
        if direction == "L":
            head[0] -= 1
            if (tail[1] == head[1]):
                if(not istouchinghorizont(tail, head)):
                    tail[0] -= 1
            elif (not istouchinghorizont(tail, head)):
                tail[0] -= 1
                tail[1] = head[1]
        if direction == "U":
            head[1] += 1
            if (tail[0] == head[0]):
                if(not istouchingvert(tail, head)):
                    tail[1] += 1
            elif (not istouchingvert(tail, head)):
                tail[1] += 1
                tail[0] = head[0]
        if direction == "D":
            head[1] -= 1
            if (tail[0] == head[0]):
                if(not istouchingvert(tail, head)):
                    tail[1] -= 1
            elif (not istouchingvert(tail, head)):
                tail[1] -= 1
                tail[0] = head[0]
        if tail not in visited:
            visited.append([tail[0], tail[1]])

def partOne(file):
    currentHead = [0,0]
    currentTail = [0,0]
    for item in file:
        step(currentTail, currentHead, item[0], item[1])

    return len(visited)

def partTwo(file):
    return 0

if __name__ == '__main__':
    file = Helpers.utils.fileToListSplit("input.txt", " ")
    Helpers.utils.debug2("Day 9, Part 1: ", partOne(file))
    Helpers.utils.debug2("Day 9, Part 2: ", partTwo(file))
