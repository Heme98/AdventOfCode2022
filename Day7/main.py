# AoC 2022 - Heme98
import Helpers.utils

class Directory:
    def __init__(self, parent, name, storage=0):
        self.parent = parent
        self.name = name
        self.storage = storage
        self.children = []

def build(input):
    root = Directory(None, "root")
    curr = root  # set current directory to root
    for item in input:
        data = item.split(" ")  # split the input
        if data[0] == "$" and data[1] == "cd" and data[2] == "..":  # exit directory
            curr = curr.parent
        elif data[0] == "$" and data[1] == "cd" and data[2] != "/":  # enter directory
            curr = [d for d in curr.children if d.name == data[2]][0]
        elif data[0] == "dir" or data[0].isdigit():  # if file or directory (the add to current directory)
            size = int(data[0]) if data[0].isdigit() else 0
            curr.children.append(Directory(curr, data[1], size))  # In this case, file is just a directory with a size
    return root

def calculateStorage(root, storage):
    return calculateSubStorage(root, storage), storage  # return total storage and list of storage for subdirectories

def calculateSubStorage(root, sizes):  # recursively go through each directory (when leaf reached return size)
    val = sum(calculateSubStorage(child, sizes) if child.children else child.storage for child in root.children)
    sizes.append(val)  # finished calulating directory size, append to sizes
    return val

def partOne(file):
    return sum(x for x in calculateStorage(build(file),[])[1] if x < 100000)

def partTwo(file):
    total, storage = calculateStorage(build(file), [])
    return min(x for x in storage if x + (70000000 - total) > 30000000)

if __name__ == '__main__':
    file = Helpers.utils.fileToListStrip("input.txt")
    Helpers.utils.debug2("Day 7, Part 1: ", partOne(file))
    Helpers.utils.debug2("Day 7, Part 2: ", partTwo(file))