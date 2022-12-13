# AoC 2022 - Heme98
import Helpers.utils
import json
import functools

def compare(a, b):
    if isinstance(a, list) and isinstance(b, list):
        for x, y in zip(a, b):
            check = compare(x, y)
            if check:
                return check
        return len(a) - len(b)
    elif isinstance(a, list):
        return compare(a, [b])
    elif isinstance(b, list):
        return compare([a], b)
    return a - b

def search(file):
    pairs, final = [], []
    for item in file:
        if item == "":
            final.append(pairs)
            pairs = []
        else:
            pairs.append(json.loads(item))
    final.append(pairs)
    return final

def partOne(file, value=0):
    pairs = search(file)
    for i, (a, b) in enumerate(pairs):
        if compare(a, b) < 0:  # if less then zero we are in right order
            value += i + 1  # add index + 1 to get position
    return value

def partTwo(file):
    pairs = search(file)
    flat_list = [item for sublist in pairs for item in sublist]
    flat_list.append([[2]])
    flat_list.append([[6]])
    flat_list.sort(key=functools.cmp_to_key(compare))
    return (flat_list.index([[2]]) + 1) * (flat_list.index([[6]]) + 1)

if __name__ == '__main__':
    file = Helpers.utils.fileToListStrip("input.txt")
    Helpers.utils.debug2("Day 13, Part 1: ", partOne(file))
    Helpers.utils.debug2("Day 13, Part 2: ", partTwo(file))
