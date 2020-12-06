def load_file(file_name: str) -> list:
    """Loads and parses the input for use in the challenge."""
    input = []
    with open(file_name) as file:
        for line in file:
            input.append(parse_ticket(line))
    return input

def parse_ticket(ticket: str) -> int:
    """Parses a ticket and returns a binary representation of it."""
    to_binary = str.maketrans("FBLR", "0101")
    binary = ticket.translate(to_binary)
    return int(binary, base=2)

def find_empty_seat(seat_ids: list) -> int:
    """Finds the empty seat id by finding the difference between a sum of all 
    seat ids within the range and the sum of all seat ids in seat_ids. 
    """
    expected = sum(range(min(seat_ids), max(seat_ids) + 1))
    current = sum(seat_ids)
    return expected - current

def parse_ticket_two(ticket: str) -> int:
    r = [0, 2 ** len(ticket.strip())]
    for i in ticket:
        if i in ["B", "R"]:
            r[0] += (r[1]-r[0]) >> 1
        elif i in ["L", "F"]:
            r[1] -= (r[1]-r[0]) >> 1
    # print(r)
    return r[0]


def main() -> None:
    """The main function for day 5. Answers Question 1 and 2."""
    tickets = load_file("day5.txt")
    empty_seat = find_empty_seat(tickets)

    print(f"Total number of tickets: {len(tickets)}")
    print(f"Maximum seat ID: {max(tickets):>11}")
    print(f"Empty seat ID: {empty_seat:>13}")

if __name__ == "__main__":
    main()