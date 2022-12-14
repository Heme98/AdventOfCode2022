# AoC 2022 - Heme98
import Helpers.utils

def istouching(tail, head):
    return (abs(tail[0] - head[0]) in [0, 1]) and (abs(tail[1] - head[1]) in [0, 1])

def move(rope, direction):
    rope[0] += 1 if direction == "R" else 0
    rope[0] -= 1 if direction == "L" else 0
    rope[1] += 1 if direction == "U" else 0
    rope[1] -= 1 if direction == "D" else 0

def step(visited, ropes, direction, amount):
    for _ in range(amount):
        for j in range(len(ropes)):
            if j == 0:
                move(ropes[j], direction) # Update Head
            elif not istouching(ropes[j], ropes[j-1]): # if not touching, update following knots
                if ropes[j][1] != ropes[j-1][1]:
                    vertical = "U" if ropes[j][1] < ropes[j - 1][1] else "D"
                    move(ropes[j], vertical)
                if ropes[j][0] != ropes[j - 1][0]:
                    horizontal = "R" if ropes[j][0] < ropes[j - 1][0] else "L"
                    move(ropes[j], horizontal)
            if [ropes[-1][0],ropes[-1][1]] not in visited: # last knot (tail) to visited
                visited.append([ropes[-1][0], ropes[-1][1]])

def partOne(file):
    visited, ropes = [], [[0, 0], [0, 0]]
    for item in file:
        step(visited, ropes, item[0], int(item[1]))
    return len(visited)

def partTwo(file):
    visited, ropes = [], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    for item in file:
        step(visited, ropes, item[0], int(item[1]))
    return len(visited)

if __name__ == '__main__':
    file = Helpers.utils.fileToListSplit("input.txt", " ")
    Helpers.utils.debug2("Day 9, Part 1: ", partOne(file))
    Helpers.utils.debug2("Day 9, Part 2: ", partTwo(file))
