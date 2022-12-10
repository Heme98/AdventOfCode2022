# AoC 2022 - Heme98
import Helpers.utils

visited = []
scenic = []

def leftandright(file, row):
    visited.append((row, 0))  # add left edge
    visited.append((row, len(file[0]) - 1))  # add right edge
    left = [(row,i) for i in range(1, len(file[0]) - 2) if file[row][i] > max(file[row][:i])]
    right = [(row,i) for i in range(len(file[0]) - 2, 1, -1) if file[row][i] > max(file[row][i+1:])]
    visited.extend(left + right)

def upanddown(file, row):
    visited.append((0, row))  # add top edge
    visited.append((len(file) - 1, row))  # add bottom edge
    down = [(i,row) for i in range(1, len(file[0]) - 2) if file[row][i] > max(file[row][:i])]
    up = [(i,row) for i in range(len(file[0]) - 2, 1, -1) if file[row][i] > max(file[row][i+1:])]
    visited.extend(down + up)

def search(file):
    visited.extend([(0,0),(len(file)-1,0),(0, len(file[0])-1),(len(file)-1,len(file[0])-1)])
    for row in range(len(file)):
        leftandright(file,row)
        upanddown(list(zip(*file)), row) # transpose vertical column to horizontal

def calculateScenic(file, row, col, t_row, t_col, roff, coff, dir = 0):
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
    Helpers.utils.debug2("Day 8, Part 1: ", partOne(file))
    Helpers.utils.debug2("Day 8, Part 2: ", partTwo(file))
