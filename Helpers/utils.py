# Generic printer function to convert all types to string and print them
def debug(value):
    print(value)

# Generic printer function with added string message
def debug2(string, value):
    print(string + str(value))

# Read file line by line and store it in a str
def fileToString(name):
    return "".join([line.strip() for line in open(f"{name}.txt", "r")])

# Read file line by line and store it in a list
def fileToListStrip(name):
    return [line.strip() for line in open(f"{name}.txt", "r")]

# Read file line by line and store it in a list
def fileToListNoStrip(name):
    return list(open(f"{name}.txt", "r"))

# Read file line by line and store it in a list
def fileToListReplaceStrip(name, old, new):
    return [line.replace(old, new).strip() for line in open(f"{name}.txt", "r")]

# Read file line by line and store it in a list
def fileToListSplit(name, split):
    return [line.strip().split(split) for line in open(f"{name}.txt", "r")]

# Read file line by line and store it in a set
def fileToSet(name):
    return {line.split() for line in open(f"{name}.txt", "r")}
