import sys

def main() -> None:
    data: list[str] = sys.stdin.readlines()

    seen: set = set((0, 0))
    x, y = 0, 0

    directions: dict[str, int] = {
        '^': -1,
        'v': 1,
        '>': 1,
        '<': -1
    }

    for idx, santa in enumerate(data[0], 2):
        if santa in ['^', 'v']:
            x += directions[santa]
            seen.add((x, y))
        else:
            y += directions[santa]
            seen.add((x, y))
    print(len(seen))

    
if __name__ == '__main__':
    main()