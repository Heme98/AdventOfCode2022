# Generic printer function to convert all types to string and print them
def debug(value):
    print(str(value))

# Generic printer function with added string message
def debug2(string, value):
    print(string + str(value))

# Read file line by line and store it in a list
def fileToList(name):
    return [line.strip() for line in open(f"{name}.txt", "r")]

# Read file line by line and store it in a set
def fileToSet(name):
    return set(line.split() for line in open(f"{name}.txt", "r"))
