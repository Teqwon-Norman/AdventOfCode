import sys
from collections import deque

def main():
    data = deque(map(int, sys.stdin.read().strip().split()))
    lookup = {}

    for _ in range(75):
        size = len(data)
        for _ in range(size):
            curr = data.popleft()

            if curr in lookup:
                data.extend(lookup[curr])

            elif curr == 0:
                lookup[curr] = [1]
                data.append(1)

            elif len(str(curr)) % 2 == 0:
                num_digits = len(str(curr)) // 2
                divider = 10**num_digits
                first, second = curr // divider, curr % divider

                lookup[curr] = [first, second]
                data.extend([first, second])

            else:
                result = curr * 2024
                lookup[curr] = [result]
                data.append(result)

    print(len(data))

if __name__ == '__main__':
    main()
