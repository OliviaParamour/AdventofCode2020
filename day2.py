import re


def load_file(file_name: str) -> list:
    """Loads and parses the input for use in the challenge."""
    input = []
    with open(file_name) as file:
        for line in file:
            parts = re.match(r"^(\d+)-(\d+) ([a-z]): (\w+)$", line)
            input.append((int(parts.group(1)), int(parts.group(2)),
                          parts.group(3), parts.group(4)) )
    return input

def is_password_valid(case: tuple) -> bool:
    """Checks if a password is valid based on provided criteria:
    Includes number of letters between low and high, inclusive.
    """
    low, high, letter, password = case[0], case[1], case[2], case[3]
    return low <= password.count(letter) <= high

def is_password_valid_two(case: tuple) -> bool:
    """Checks if a password is valid based on provided criteria:
    Must contain a letter in either position 1 or 2 but not both.
    """
    first, second, criteria, password = case[0]-1, case[1]-1, case[2], case[3]
    return (password[first] == criteria) ^ (password[second] == criteria)


def main() -> None:
    """The main function for day 2. Answers question 1 and 2."""
    passwords = load_file("day2.txt")
    
    schema_1 = sum([is_password_valid(password) for password in passwords])
    schema_2 = sum([is_password_valid_two(password) for password in passwords])
    
    print(f"Total Passwords: {len(passwords)}")
    print( f"Number of valid passwords for schema 1: {schema_1}" )
    print(f"Number of valid passwords for schema 2: {schema_2}" )

if __name__ == "__main__":
    main()