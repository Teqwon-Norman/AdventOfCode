from itertools import batched
import sys

def main() -> None:
    data: list[str] = sys.stdin.readlines()

    seen: set = set((0, 0))
    sx, sy, rx, ry = 0, 0, 0, 0

    directions: dict[str, int] = {
        '^': -1,
        'v': 1,
        '>': 1,
        '<': -1
    }

    for idx, (santa, robo) in enumerate(batched(data[0], 2)):
        if santa in ['^', 'v']:
            sx += directions[santa]
            seen.add((sx, sy))
        else:
            sy += directions[santa]
            seen.add((sx, sy))
        
        if robo in ['^', 'v']:
            rx += directions[robo]
            seen.add((rx, ry))
        else:
            ry += directions[robo]
            seen.add((rx, ry))

    res: int = 0
    for i in seen:
        if isinstance(i, tuple):
            res += 1

    print(res)
if __name__ == '__main__':
    main()