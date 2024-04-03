from itertools import batched

import math
import sys

def find_minimum(cubes: list[str]) -> int:
    red_max = green_max = blue_max = 0

    for count, color in batched(cubes, 2):
        match color[0]:
            case "r":
                red_max = max(red_max, int(count))
            case "g":
                green_max = max(green_max, int(count))
            case "b":
                blue_max = max(blue_max, int(count))
            case _:
                raise ValueError(f"Invalid color: {color}")
    return math.prod( [red_max, green_max, blue_max] )

def main() -> None:
    result: int = 0

    for line in sys.stdin:
        _, _, *cubes = line.split()
        result += find_minimum(cubes)
    print(result)

if __name__ == '__main__':
    main()
