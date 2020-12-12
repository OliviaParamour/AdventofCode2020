from enum import Enum
from typing import List


def load(file_name: str) -> list:
    """Loads and parses the input for use in the challenge."""
    input = []
    with open(file_name) as file:
        for line in file:
            direction = line[0]
            magnitude = int(line[1:])
            input.append({"direction": Heading[direction].value,
                          "magnitude": magnitude})
    return input

class Heading(Enum):
    N = (0, 1)
    S = (0, -1)
    E = (1, 0)
    W = (-1, 0)
    L = -1
    R = 1
    F = 0
    def find_name(self, value):
        pass

class Ship():
    def __init__(self, heading=Heading.E.value , waypoint:tuple=(10,1)) -> None:
        super().__init__()
        self.heading = heading
        self.x = 0
        self.y = 0
        self.waypoint = waypoint
    
    def __repr__(self) -> str:
        return_string = f"This ship is currently at {self.x}, {self.y}, "
        return_string += f"heading: {self.get_heading()}"
        return return_string
    def traverse(self, inputs: list):
        for input in inputs:
            direction = input["direction"]
            magnitude = input["magnitude"]
            if direction == 0:
                print(f"Ship moved {self.get_heading()} {magnitude}")
                self.x += magnitude * self.waypoint[0]
                self.y += magnitude * self.waypoint[1]
                print(self.x, self.y) 
            elif direction not in (-1, 1):
                print(f"Waypoint moved {self.get_heading()} {magnitude}")
                x, y = self.move(direction, magnitude)
                self.waypoint = (x + self.waypoint[0], y + self.waypoint[1])
                print(self.waypoint) 
                print(self.x, self.y) 
            else:
                print(f"Ship rotated {self.get_heading()} {magnitude}")
                self.heading = self.rotate(self.heading, direction, magnitude)
                self.waypoint = self.rotate(self.waypoint, direction, magnitude)
                print(self.waypoint)
                print(self.x, self.y)

    def move(self, heading: tuple, magnitude: int):
        return tuple([i * magnitude for i in heading])

    def rotate(self, heading: tuple, rotation: int , magnitude: int) -> tuple:
        angle = (360 + magnitude * rotation) % 360
        if angle == 90:
            return (heading[1], -heading[0])
        elif angle == 180:
            return (-heading[0], -heading[1])
        elif angle == 270:
            return (-heading[1], heading[0])
        return heading

    def manhatten_distance(self):
        return abs(self.x) + abs(self.y)
    
    def reset(self):
        self.heading = Heading.E.value
        self.x = 0
        self.y = 0
        self.waypoint = (10, 0)

    def get_heading(self):
        headings = {(0, 1): "North", (0, -1): "South",
                    (1, 0): "East", (-1, 0): "West"}
        return headings[self.heading]


def main() -> None:
    """The main function for day 12. Answers Question 1 and 2."""
    inputs = load("day12.txt")
    Ferry = Ship(waypoint =(10, 1))
    print(f"Total number of inputs: {len(inputs)}")
    Ferry.traverse(inputs)
    print(Ferry)
    print(f"Distance travlled by {Ferry.manhatten_distance()}")

if __name__ == "__main__":
    main()