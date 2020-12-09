import itertools

def load(file_name: str) -> list:
    """Loads and parses the input for use in the challenge."""
    input = []
    with open(file_name) as file:
        for line in file:
            input.append(int(line.strip()))
    return input

def find_invalid(num: list, num_range: int) -> int:
    for i in range(num_range, len(num)):
        num_list = num[i-num_range:i]
        combinations = list(itertools.combinations(num_list, 2))
        if num[i] not in map(sum, combinations):
            return num[i]
    return -1


def main() -> None:
    """The main function for day 9. Answers Question 1 and 2."""
    numbers = load("day9a.txt")
    number_range = 5
    invalid_number = find_invalid(numbers, number_range)
    print(f"Total number of inputs: {len(numbers)}")
    # [print(input) for number in numbers]
    print(f"Invalid number: {invalid_number}")

if __name__ == "__main__":
    main()