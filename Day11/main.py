# AoC 2022 - Heme98
import Helpers.utils
import operator
from math import prod

ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

class Monkey:
    def __init__(self):
        self.items = []
        self.operation = []
        self.test = 0
        self.direction = []
        self.throws = 0

def createMonkeys(file):
    monkeys = []
    for row in file:
        if row != "":
            if "Monkey" in row:
                monkeys.append(Monkey())
            elif "Starting items" in row:
                monkeys[-1].items = [x for x in row.replace(",", " ").split(" ") if x.isdigit()]
            elif "Operation" in row:
                monkeys[-1].operation = row.split(" ", 4)[4].split()
            elif "Test" in row:
                monkeys[-1].test = int(row.rsplit(" ", 1)[1])
            else:
                monkeys[-1].direction.append(int(row.rsplit(" ", 1)[1]))
    return monkeys

def getMonkeyBusiness(monkeys, rounds, commonMod, relief):
    for _ in range(rounds):
        for monkey in monkeys:
            for item in monkey.items:
                monkey.throws += 1
                test = int(monkey.operation[1]) if monkey.operation[1] != "old" else int(item)
                res = (ops[monkey.operation[0]](int(item), test) // relief) % commonMod
                if res % monkey.test == 0:
                    monkeys[monkey.direction[0]].items.append(res)
                else:
                    monkeys[monkey.direction[1]].items.append(res)
            monkey.items.clear()
    mostActive = sorted([monkey.throws for monkey in monkeys])[-2:]
    return mostActive[0] * mostActive[1]

def partOne(file,rounds, relief):
    monkeys = createMonkeys(file)
    commonMod = prod(m.test for m in monkeys)
    return getMonkeyBusiness(monkeys, rounds, commonMod, relief)

def partTwo(file,rounds, relief):
    monkeys = createMonkeys(file)
    commonMod = prod(m.test for m in monkeys)
    return getMonkeyBusiness(monkeys, rounds, commonMod, relief)

if __name__ == '__main__':
    file = Helpers.utils.fileToListReplaceStrip("input.txt", ":", "")
    Helpers.utils.debug2("Day 11, Part 1: ", partOne(file, 20, 3))
    Helpers.utils.debug2("Day 11, Part 2: ", partTwo(file, 10000, 1))