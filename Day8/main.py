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
    visited.extend([(0,0),(len(file)-1,0),(0, len(file[0])-1),(len(file)-1,len(file[0])-1)])
    for col in range(len(file[0])):
        if col not in [0, len(file[0]) - 1]:
            visited.append((0, col))  # add top edge
            visited.append((len(file) - 1, col))  # add bottom edge
            upanddown(0, col, file, 0, col, False)  # Look down
            upanddown(0, col, list(reversed(file)), 0, col, True)  # Look up
    for row in range(len(file)):
        if row not in [0, len(file) - 1]:
            visited.append((row, 0))  # add left edge
            visited.append((row, len(file[0]) - 1))  # add right edge
            leftandright(row, 0, file, row, 0, False)  # Look right
            leftandright(row, 0, [list(reversed(new)) for new in file], row, 0, True)  # Look left

def calculateScenic(file, row, col, t_row, t_col, roff, coff):
    dir = 0
    while t_row != 0 and t_row != len(file) - 1 and t_col != 0 and t_col != len(file[0]) - 1:
        dir += 1
        if file[row][col] <= file[t_row + roff][t_col + coff]:
            break
        t_row += roff
        t_col += coff
    return dir

def getScenic(file):
    for item in visited:
        row, col = item[0], item[1]
        up = calculateScenic(file, row, col, row, col, -1, 0)
        down = calculateScenic(file, row, col, row, col, 1, 0)
        left = calculateScenic(file, row, col, row, col, 0, -1)
        right = calculateScenic(file, row, col, row, col, 0, 1)
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
