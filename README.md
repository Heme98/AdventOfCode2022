# AdventOfCode2022

This is my attempt at solving [Advent of Code 2022](https://adventofcode.com/) in Python. Feel free to take a look and get inspired 

## Helpers

All classes might make use of some helper functions defined in [Helpers/util.py](https://github.com/Heme98/AdventOfCode2022/blob/main/Helpers/utils.py)

In the code, simply write the following to access the helper functions

```python
import Helpers.utils

def loadFile(filename):
    string = Helpers.utils.fileToString(filename)
    set = Helpers.utils.fileToSet(filename)
```
In this case, I will mainly have functions to parse files and print certain object but it may get extended depending on the task at hand.

## Benchmarking

Additionaly, some benchmarking functions will be implemented to test the performance
of the solutions for each of the different days.

## Todo

Add some .sh or .py scripts to automate project structure generation and/or other things...

Add benchmarking to log the time of each test run

Might do some code refactoring depending on how much I like my solutions or not

