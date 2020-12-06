import math


def load_file(file_name: str) -> list:
    """Loads and parses the input for use in the challenge."""
    input = []
    with open(file_name) as file:
        for line in file:
            input.append(line.strip())
    return input

def traverse(field: list, right=3, down=1) -> int:
    """Counts all trees hit at each step on a slope, right and down."""
    length = len(field)
    width = len(field[0])
    number_of_trees = 0
    for i in range(0, length, down):
        spot = field[i][i // down * right % width]
        if spot == "#":
            number_of_trees += 1
    return number_of_trees

def traverse_all_slopes(field, slopes) -> list:
    """Counts all trees hit by each slope in slopes."""
    total_trees = []
    for slope in slopes:
        total_trees.append(traverse(field, slope[0], slope[1]))
    return total_trees


def main() -> None:
    """The main function for day 3. Answers question 1 and 2."""
    slopes = [(1, 1), (3, 1), (5, 1) , (7, 1), (1, 2)]
    
    field = load_file("day3.txt")
    trees_for_slope_three_one = traverse(field, 3, 1)
    total_trees = traverse_all_slopes(field, slopes)
    multiplied_total = math.prod(total_trees)

    print(f"Field Width: {len(field[0]):>7}")
    print(f"Field Height: {len(field):>6}\n")
    print(f"Sum of three hit on slope, (3,1): {trees_for_slope_three_one:>19}")
    print(f"product of sum of trees hit on all slopes: {multiplied_total:>10}")

if __name__ == "__main__":
    main()