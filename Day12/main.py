# AoC 2022 - Heme98
import Helpers.utils
import copy

def findStartAndEnd(file):
    points = {"start": None, "end": None}
    starts = []
    for row in range(len(file)):
        for col in range(len(file[0]) - 1):
            if file[row][col] == "S":
                points["start"] = (row,col)
                starts.append((row,col))
                file[row] = file[row].replace("S", "a")
            elif file[row][col] == "E":
                points["end"] = (row,col)
                file[row] = file[row].replace("E","z")
            elif file[row][col] == 'a':
                starts.append((row, col))

    result = bfs(file, points["end"])
    totals = [result.get(point) for point in starts if result.get(point)]
    return [result[points["start"]], min(totals)]

def bfs(matrix, end):
    queue = [end]
    distance = {end: 0}
    while queue:
        x, y = queue.pop(0)
        neighbors = []
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (0 <= nx < len(matrix)) and (0 <= ny < len(matrix[0])) and ord(matrix[x][y]) - 1 <= ord(matrix[nx][ny]):
                neighbors.append((nx, ny))

        for neighbor in neighbors:
            if neighbor not in distance:
                distance[neighbor] = distance[(x,y)] + 1
                queue.append(neighbor)
    return distance

def partOne(file):
    return findStartAndEnd(file)[0]

def partTwo(file):
    return findStartAndEnd(file)[1]

if __name__ == '__main__':
    file = Helpers.utils.fileToListReplaceStrip("input.txt", ":", "")
    Helpers.utils.debug2("Day 12, Part 1: ", partOne(copy.deepcopy(file)))
    Helpers.utils.debug2("Day 12, Part 2: ", partTwo(copy.deepcopy(file)))