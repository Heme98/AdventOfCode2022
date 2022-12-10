# AoC 2022 - Heme98
import Helpers.utils

visited = []

def istouchinghorizont(tail, head):
    return abs(tail[0] - head[0]) in [0, 1]

def istouchingvert(tail, head):
    return abs(tail[1] - head[1]) in [0, 1]

def move(rope, direction):
    if direction == "R":
        rope[0] += 1
    if direction == "L":
        rope[0] -= 1
    if direction == "U":
        rope[1] += 1
    if direction == "D":
        rope[1] -= 1

def step(ropes, direction, amount):
    for _ in range(amount):
        for j in range(len(ropes)):
            if j == 0:
                move(ropes[j], direction) # Update Head
            elif not istouchinghorizont(ropes[j], ropes[j-1]):
                if ropes[j][1] != ropes[j-1][1]:
                    vertical = "U" if ropes[j][1] < ropes[j - 1][1] else "D"
                    move(ropes[j], vertical)
                if ropes[j][0] != ropes[j - 1][0]:
                    horizontal = "R" if ropes[j][0] < ropes[j - 1][0] else "L"
                    move(ropes[j], horizontal)
            elif not istouchingvert(ropes[j], ropes[j-1]):
                if ropes[j][1] != ropes[j - 1][1]:
                    vertical = "U" if ropes[j][1] < ropes[j - 1][1] else "D"
                    move(ropes[j], vertical)
                if ropes[j][0] != ropes[j-1][0]:
                    horizontal = "R" if ropes[j][0] < ropes[j - 1][0] else "L"
                    move(ropes[j], horizontal)
            if [ropes[-1][0],ropes[-1][1]] not in visited:
                visited.append([ropes[-1][0], ropes[-1][1]])

def partOne(file):
    ropes = [[0, 0], [0, 0]]
    for item in file:
        step(ropes, item[0], int(item[1]))
    return len(visited)

def partTwo(file):
    ropes = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    visited.clear()
    for item in file:
        step(ropes, item[0], int(item[1]))
    return len(visited)

if __name__ == '__main__':
    file = Helpers.utils.fileToListSplit("input.txt", " ")
    Helpers.utils.debug2("Day 9, Part 1: ", partOne(file))
    Helpers.utils.debug2("Day 9, Part 2: ", partTwo(file))
