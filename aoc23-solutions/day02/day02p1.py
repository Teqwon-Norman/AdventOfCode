from itertools import batched
import sys

RED = 12
GREEN = 13
BLUE = 14

def is_possible(count: str, color: str) -> bool:
    """match the color to a case and return a boolean."""
    match color:
        case "r":
            return int(count) <= RED
        case "g":
            return int(count) <= GREEN
        case "b":
            return int(count) <= BLUE
        case _:
            raise ValueError(f"Invalid color: {color}")

def main():
    result: int = 0

    for idx, line in enumerate(sys.stdin):
        _, _, *cubes = line.split()
        if all( is_possible(count, color[0]) for count, color in batched(cubes, 2) ):
            result += idx + 1
    print(result)

if __name__ == "__main__":
    main()
