import sys
from collections import deque

cache = {}

def dfs(blinks, stone):
    if blinks == 0:
        return 1

    res = cache.get((blinks, stone))
    if res:
        return res

    if stone == 0:
        res = dfs(blinks-1, 1)

    elif len(str(stone)) % 2 == 0:
        num_digits = len(str(stone)) // 2
        divider = 10**num_digits
        first, second = stone // divider, stone % divider
        res = dfs(blinks-1, first) + dfs(blinks-1, second)
    else:
        res = dfs(blinks-1, stone * 2024)

    cache[(blinks, stone)] = res
    return res

def main():
    data = deque(map(int, sys.stdin.read().strip().split()))
    res = 0
    for curr in data:
        res += dfs(75, curr)
    print(res)

if __name__ == '__main__':
    main()
