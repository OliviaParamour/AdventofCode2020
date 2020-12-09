import itertools
from collections import deque

def load(file_name: str) -> list:
    """Loads and parses the input for use in the challenge."""
    input = []
    with open(file_name) as file:
        for line in file:
            input.append(int(line.strip()))
    return input

def find_invalid(numbers: list, num_range: int) -> int:
    for i in range(num_range, len(numbers)):
        num_list = numbers[i-num_range:i]
        combinations = list(itertools.combinations(num_list, 2))
        if numbers[i] not in map(sum, combinations):
            return numbers[i]
    return -1

def find_contiguous_range(numbers: list, invalid_number: int) -> tuple:
    index = numbers.index(invalid_number)
    stack = deque()
    for number in numbers[:index]:
        while sum(stack) > invalid_number:
            stack.popleft()
        if sum(stack) == invalid_number:
            return min(stack), max(stack)
        else:
            stack.append(number)
    return -1,-1


def main() -> None:
    """The main function for day 9. Answers Question 1 and 2."""
    numbers = load("day9.txt")
    number_range = 25
    invalid_number = find_invalid(numbers, number_range)
    max_min = find_contiguous_range(numbers, invalid_number)
    max_min_sum = sum(max_min)

    print(f"Total number of inputs: {len(numbers)}")
    print(f"Invalid number: {invalid_number}", end=" ")
    print(f"at index {numbers.index(invalid_number)}")
    print(f"Max and Min that sum to {invalid_number}: {max_min}")
    print(f"Product of {max_min[0]} and {max_min[1]}: {max_min_sum}")

if __name__ == "__main__":
    main()