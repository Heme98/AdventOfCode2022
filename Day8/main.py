# AoC 2022 - Heme98
import Helpers.utils

visited = []
scenic = []

def upanddown(i, j, file, k, l, up):  # recursive check (TODO: Remove recursion)
    if i != len(file) - 1:
        if file[k][l] < file[i][j]:
            k, l = i, j
            visited.append((len(file) - 1 - i, j)) if up else visited.append((i, j))
        return upanddown(i + 1, j, file, k, l, up)
    return k, l

def leftandright(i, j, file, k, l, left):  # recursive check (TODO: Remove recursion)
    if j != len(file[0]) - 1:
        if file[k][l] < file[i][j]:
            k, l = i, j
            visited.append((i, len(file[0]) - 1 - j)) if left else visited.append((i, j))
        return leftandright(i, j + 1, file, k, l, left)
    return k, l

def search(file):
    for row in range(len(file)):
        for col in range(len(file[0])):
            if row in [0, len(file) - 1] and col in [0, len(file[0]) - 1]:  # adding corners
                visited.append((row, col))
            if row == 0:
                visited.append((row, col))  # add top edge
                visited.append((len(file) - 1, col))  # add bottom edge
                upanddown(0, col, file, 0, col, False)  # Look down
                upanddown(0, col, list(reversed(file)), 0, col, True)  # Look up
            if col == 0 and row != 0 and row != len(file) - 1:
                visited.append((row, col))  # add left edge
                visited.append((row, len(file[0]) - 1))  # add right edge
                leftandright(row, col, file, row, col, False)  # Look right
                leftandright(row, 0, [list(reversed(new)) for new in file], row, 0, True)  # Look left

def calculateScenic(file, row, col, t_row, t_col, roff, coff, case):
    dir = 0
    while t_row != 0 and case == "up" or t_row != len(file) - 1 and case == "down" or t_col != 0 and case == "left" or t_col != len(file[0]) - 1 and case == "right":
        dir += 1
        if file[row][col] <= file[t_row + roff][t_col + coff]:
            break
        t_row += roff
        t_col += coff
    return dir

def getScenic(file):
    for item in visited:
        row, col = item[0], item[1]
        t_row, t_col = row, col
        up = calculateScenic(file, row, col, t_row, t_col, -1, 0, "up")
        down = calculateScenic(file, row, col, t_row, t_col, 1, 0, "down")
        left = calculateScenic(file, row, col, t_row, t_col, 0, -1, "left")
        right = calculateScenic(file, row, col, t_row, t_col, 0, 1, "right")
        scenic.append(up * down * left * right)

def partOne(file):
    search(file)
    return len(set(visited))

def partTwo(file):
    getScenic(file)
    return max(scenic)

if __name__ == '__main__':
    file = Helpers.utils.fileToListStrip("input.txt")
    Helpers.utils.debug2("Day 7, Part 1: ", partOne(file))
    Helpers.utils.debug2("Day 7, Part 2: ", partTwo(file))
