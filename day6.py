def load(file_name: str) -> list:
    """Loads and parses the input for use in the challenge."""
    with open(file_name) as file:
        inputs = []
        group = []
        for line in file:
            if line != "\n":  
                group.append(set(line.strip()))
            else:
                inputs.append(group)
                group = []
        inputs.append(group)
    return inputs

def get_total_yes(inputs: list) -> int:
    """Sums the questions that each group's had at least answered yes to."""
    result = 0
    for group in inputs:
        result += len(set.union(*group))
    return result

def get_total_group_yes(inputs: list) -> int:
    """Sums the questions that each group's members all answered yes to"""
    result = 0
    for group in inputs:
        result += len(set.intersection(*group))
    return result


def main() -> None:
    """The main function for day 6. Answers Question 1 and 2."""
    inputs = load("day6.txt")
    total_yes = get_total_yes(inputs)
    total_group_yes = get_total_group_yes(inputs)

    print(f"Total number of inputs: {len(inputs):>45}")
    print(f"Sum of all questions that each group said yes to: {total_yes:>19}")
    print(f"Sum of all members that said yes", end=" ")
    print(f"to the same question per group: {total_group_yes}")

if __name__ == "__main__":
    main()