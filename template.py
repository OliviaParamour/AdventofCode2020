import re
import functools
import itertools
import operator

def load(file_name: str) -> list:
    """Loads and parses the input for use in the challenge."""
    input = []
    with open(file_name) as file:
        for line in file:
            input.append(parse(line.strip()))
    return input

def parse(line: str):
    pass

def main() -> None:
    """The main function for day 4. Answers Question 1 and 2."""
    inputs = load("day5.txt")
    
    print(f"Total number of inputs: {len(inputs)}")
    [print(input) for input in inputs]

if __name__ == "__main__":
    main()