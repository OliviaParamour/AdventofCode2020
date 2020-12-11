from typing import Callable

def load(file_name: str) -> list:
    """Loads and parses the input for use in the challenge."""
    input = []
    with open(file_name) as file:
        for line in file:
            input.append(line.strip())
    return input

def check_adjacent(input: list, rows, cols):
    vectors = [(-1, 1), (0, 1), (1,1), (-1, 0),
              (1, 0), (-1,-1), (0,-1), (1,-1)]
    value = input[rows[1]][cols[1]]
    count = 0
    for row in set(rows):
        for col in set(cols):
            if input[row][col] == "#":
                count += 1
                if value == "L":
                    return "L"
    if count > 4 and value == "#":
        return "L"
    return "#"

def run_adjacent_iteration(input: list) -> list:
    next = [row.copy() for row in input]
    for row in range(len(input)):
        row_range = [max(row-1, 0), row, min(row+1, len(input)-1)]
        for col in range(len(input[row])):
            col_range = [max(col-1, 0), col, min(col+1, len(input[row])-1)]
            if input[row][col]!=".":
                next[row][col] = check_adjacent(input, row_range, col_range)
    return next

def run_ray_cast_iteration(input: list) -> list:
    next = [row.copy() for row in input]
    for row in range(len(input)):
        for col in range(len(input[row])):
            if input[row][col]!=".":
                next[row][col] = ray_cast(input, row, col)
    return next

def ray_cast(input: list, row, col):
    vectors = [(-1, 1), (0, 1), (1,1), (-1, 0),
              (1, 0), (-1,-1), (0,-1), (1,-1)]
    x, y = 0, 0
    count = 0
    for vector in vectors:
        x += vector[0]
        y += vector[1]
        if 0 <= row+x < len(input) and 0 <= col + y < len(input[row]): 
            while input[row+x][col+y] == ".":
                x += vector[0]
                y += vector[1]
                if 0 <= row+x < len(input) and 0 <= col + y < len(input[row]):
                    continue
                else:
                    x -= vector[0]
                    y -= vector[1]
                    break
        else:
            x = 0
            y = 0
        if (x != 0 or y != 0) and input[row+x][col+y] == "#":
            count += 1
        x, y = 0, 0
    if count > 4:
        return "L"
    elif count == 0:
        return "#"
    else:
        return input[row][col]

def run_iterations(input: list, func: Callable) -> list:
    previous = input
    count = 0
    while True:
        # print(f"step: {count:>2}")
        current = func(previous)
        if current == previous:
            return current
        else:
            previous = [row.copy() for row in current]
        count += 1


def main() -> None:
    """The main function for day 11. Answers Question 1 and 2."""
    inputs = load("day11.txt")
    inputs = [i.replace("#", "L") for i in inputs]
    inputs = [list(i) for i in inputs]
    print(f"Total number of inputs: {len(inputs)}")

    steps = run_iterations(inputs, run_adjacent_iteration)
    num_of_occupied = sum([str(i).count("#") for i in steps])
    print("Number of occupied:", num_of_occupied)

    steps_2 = run_iterations(inputs, run_ray_cast_iteration)
    num_of_occupied_2 = sum([str(i).count("#") for i in steps_2])
    print("Number of occupied:", num_of_occupied_2)

if __name__ == "__main__":
    main()