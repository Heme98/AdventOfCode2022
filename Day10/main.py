# AoC 2022 - Heme98
import Helpers.utils

def noop(currentCRT, regx, clock_cycles, cycles, CRT, isCRT, signals):
    if isCRT:
        currentCRT += "#" if clock_cycles in [regx - 1, regx, regx + 1] else "."
    clock_cycles += 1
    if clock_cycles in cycles:
        CRT.append(currentCRT)
        if isCRT:
            clock_cycles = 0
        currentCRT = ""
        signals.append(clock_cycles * regx)
    return currentCRT,regx, clock_cycles

def calculateSignal(file,cycles, isCRT=False):
    signals,CRT = [], []
    clock_cycles, regx = 0, 1
    currentCRT = ""
    for item in file:
        if item[0] == "addx":
            for i in range(2):
                currentCRT, regx, clock_cycles = noop(currentCRT, regx, clock_cycles, cycles, CRT, isCRT, signals)
                if i == 1:
                    regx += int(item[1])
        else:
            currentCRT, regx, clock_cycles = noop(currentCRT,regx,clock_cycles, cycles, CRT, isCRT, signals)
    return sum(signals), CRT

def partOne(file):
    cycles = [20,60,100,140,180,220]
    return calculateSignal(file, cycles)[0]

def partTwo(file):
    cycles = [40]
    print(*calculateSignal(file, cycles, True)[1], sep="\n")

if __name__ == '__main__':
    file = Helpers.utils.fileToListSplit("input.txt", " ")
    Helpers.utils.debug2("Day 10, Part 1: ", partOne(file))
    Helpers.utils.debug2("Day 10, Part 2: ", partTwo(file))
