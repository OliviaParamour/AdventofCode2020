import re


def load(file_name: str) -> dict:
    """Loads and parses the input for use in the challenge."""
    bag_rules = {}
    with open(file_name) as file:
        find_bags = re.compile(r"(\d+) ([\w\s]+) bag.")
        for line in file:
            key_bag, value_bags = line.split(" bags contain ")
            bags = re.findall(find_bags, value_bags)
            bag_rules[key_bag] = {bag[1]:int(bag[0]) for bag in bags}
    return bag_rules

def find_all_outer(bag, bag_rules) -> set:
    outer_bags = set()
    for key_bag in bag_rules:
        if bag in bag_rules[key_bag]:
            outer_bags.add((key_bag))
            outer_bags.update(find_all_outer(key_bag, bag_rules))
    if outer_bags:
        return outer_bags
    return set([bag])

def find_all_inner(bag, bag_rules) -> int:
    inner_bags = 0
    for value_bag in bag_rules[bag]:
        quantity = bag_rules[bag][value_bag]
        inner_bags += quantity
        inner_bags += quantity * find_all_inner(value_bag, bag_rules)
    return inner_bags


def main() -> None:
    """The main function for day 7. Answers Question 1 and 2."""
    bag_rules = load("day7.txt")
    bag = "shiny gold"

    all_outer_bags = len(find_all_outer(bag, bag_rules))
    all_inner_bags = find_all_inner(bag, bag_rules)
    
    print(f"Total number of bags: {len(bag_rules)}")
    print(f"Total number of outer bags for {bag}: {all_outer_bags}")
    print(f"Total number of inner bags for {bag}: {all_inner_bags}")

if __name__ == "__main__":
    main()