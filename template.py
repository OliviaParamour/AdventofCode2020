import re
import functools
import itertools
import operator

def load(file_name: str) -> list:
    """Loads and parses the input for use in the challenge."""
    input = []
    with open(file_name) as file:
        for line in file:
            input.append(line.strip())
    return input

def myfunc(input: list) -> int:
    return 0


def main() -> None:
    """The main function for day 10. Answers Question 1 and 2."""
    inputs = load("day5.txt")
    value = myfunc(inputs)

    print(f"Total number of inputs: {len(inputs)}")
    [print(input) for input in inputs]
    print(f"The value: {value}")

if __name__ == "__main__":
    main()