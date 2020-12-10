import itertools


def load_file(file_name: str) -> list:
    """Loads and parses the input for use in the challenge."""
    numbers = []
    with open(file_name) as file:
        numbers = [int(line) for line in file]
    return numbers

def find_two_sum(numbers: list, limit: int) -> list:
    """Find two numbers in a list that sum to the limit"""
    found = []
    low_numbers = [i for i in numbers if i <= limit/2]
    for a in low_numbers:
        if (b := (limit-a)) in numbers:
            found.append(a * b)
    return found

def find_three_sum(numbers: list, limit: int) -> list:
    """Find three numbers in a list that sum to the limit"""
    found = []
    low_numbers = [i for i in numbers if i < limit/2]
    for a, b in itertools.combinations(low_numbers, 2):
        if (c := (2020 - a - b)) in numbers:
            found.append(a * b * c)
    return found


def main() -> None:
    """The main function for day 1. Answers question 1 and 2."""
    numbers = load_file("day1.txt")
    found_two = find_two_sum(numbers, 2020)
    found_three = find_three_sum(numbers, 2020)

    print(f"Total numbers in input: {len(numbers)}")
    print(f"Two numbers multiply up to {found_two[0]}")
    print(f"Thee numbers multiply up to {found_three[0]}")

if __name__ == "__main__":
    main()