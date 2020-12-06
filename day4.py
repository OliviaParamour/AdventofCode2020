import re


def load_file(file_name: str) -> list:
    """Loads and parses the input for use in the challenge."""
    passports = []
    with open(file_name) as file:
        passport = {}
        for line in file:
            if line != "\n":
                items = re.findall(r"([^ ]+):([\S]+)", line)
                passport.update(items)
            else:
                passports.append(passport)
                passport = {}
        passports.append(passport)
    return passports

def is_valid(keys: set) -> bool:
    """Checks if keys contain the required keys."""
    required = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    return required <= keys

def is_all_valid(passports: list) -> tuple:
    """Checks if all keys are in each passport and
    that their values meets eachkeys' criteria.
    """
    count = 0
    count2 = 0
    for passport in passports:
        valid = is_valid(passport.keys())
        count += valid
        if valid:
            valid &= check_value(passport["byr"], 1920, 2002)
            valid &= check_value(passport["iyr"], 2010, 2020)
            valid &= check_value(passport["eyr"], 2020, 2030)
            valid &= check_height(passport["hgt"])
            valid &= check_hair_colour(passport["hcl"])
            valid &= check_eye_colour(passport["ecl"])
            valid &= check_pid(passport["pid"])
            
            count2 += valid
    return count, count2

def check_value(value: str, low: int, high: int) -> bool:
    return low <= int(value) <= high

def check_height(height: str) -> bool:
    if height.endswith("in"):
        return check_value(height[:-2], 59, 76)
    elif height.endswith("cm"):
        return check_value(height[:-2], 150, 193)
    return False

def check_hair_colour(colour: str) -> bool:
    return bool(re.match(r"#[0-9a-f]{6}", colour))
    
def check_eye_colour(colour: str) -> bool:
    valid_colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return  colour in valid_colours

def check_pid(pid: str) -> bool:   
    return len(pid) == 9 and pid.isdigit()


def main() -> None:
    """The main function for day 4. Answers Question 1 and 2."""
    passports = load_file("day4.txt")
    valid_passports = is_all_valid(passports)
    
    print(f"Total number of passports: {len(passports)}")
    print(f"Number of valid passwords for test one: {valid_passports[0]}")
    print(f"Number of valid passwords for test two: {valid_passports[1]}")

if __name__ == "__main__":
    main()