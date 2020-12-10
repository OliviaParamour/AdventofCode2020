import numpy
import collections

def load(file_name: str) -> list:
    """Loads and parses the input for use in the challenge."""
    input = []
    with open(file_name) as file:
        for line in file:
            input.append(int(line))
    return input

def count_groups_by_number_of_consecutive_ones(input: list) -> list:
    consecutive_ones = []
    count_one = 0
    for i in input:
        if i == 1:
            count_one += 1
        elif count_one > 0:
            consecutive_ones.append(count_one)
            count_one = 0
    return consecutive_ones

def find_number_of_permutations(c_ones: list) -> int:
    c_ones_by_grp = collections.Counter(c_ones)
    trib = [0, 0, 1]
    total = 1
    for i in range(len(c_ones_by_grp)):
        trib.append(sum(trib[0+i:3+i]))
        total *= trib[-1] ** c_ones_by_grp[i+1]
    return total


def main() -> None:
    """The main function for day 10. Answers Question 1 and 2."""
    inputs = load("day10.txt")
    inputs.extend([0, max(inputs)+3])
    inputs.sort()

    difference = numpy.diff(inputs)
    count = collections.Counter(difference)
    consecutive_ones = count_groups_by_number_of_consecutive_ones(difference)
    total = find_number_of_permutations(consecutive_ones)

    print(f"Total number of inputs: {len(inputs)}")
    print(f"The values: {count[1]}, {count[3]}")
    print(f"The product: {count[1] * count[3]}")
    print(f"Total permutations: {total}")

if __name__ == "__main__":
    main()