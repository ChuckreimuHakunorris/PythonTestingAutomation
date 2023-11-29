import json
import random
import os
import sys


class exampleClass:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def add(self):
        sum = self.val1 + self.val2
        print("Sum is:", sum)


def another_function():
    print("This function does nothing useful")


example = exampleClass(5, 10)
example.add()

for i in range(0, 10):
    print(i)


def unused_function():
    pass


# Badly formatted dictionary
example_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Unused imports

# Too many blank lines