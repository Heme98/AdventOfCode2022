# AoC 2022 - Heme98
import Helpers.utils
import copy

def condRev(stack, single):
    return reversed(stack) if single else stack  # single crates will not keep order and should be reversed at the end

def buildAndMove(stack, key, moves, singlecrate):
    ship = [[crate[i] for crate in reversed(stack) if crate[i] != "."] for i in range(len(key)) if key[i] != "."]
    orders = [[int(_) for _ in move.split(".") if _.isdigit()] for move in moves]  # Parse instruction
    for ord in orders:
        ship[ord[2]-1].extend(condRev(ship[ord[1]-1][len(ship[ord[1]-1])-ord[0]:], singlecrate))  # add to new stack
        ship[ord[1]-1] = ship[ord[1]-1][:len(ship[ord[1]-1])-ord[0]]
    return "".join([ship[i].pop() for i in range(len(ship))])

def partOne(ship, index, instructions):
    return buildAndMove(copy.deepcopy(ship), index, instructions, singlecrate=True)

def partTwo(ship, index, instructions):
    return buildAndMove(copy.deepcopy(ship), index, instructions, singlecrate=False)

if __name__ == '__main__':
    file = Helpers.utils.fileToListReplaceStrip("input", " ", ".")
    ship,key,moves = file[:file.index("")-1], file[file.index("")-1], file[file.index("")+1:]
    Helpers.utils.debug2("Day 5, Part 1: ", partOne(ship, key, moves))
    Helpers.utils.debug2("Day 5, Part 2: ", partTwo(ship, key, moves))
