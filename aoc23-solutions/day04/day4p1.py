import sys

def main() -> None:
    result: int = 0

    for line in sys.stdin.readlines():
        winners, numbers = line.split(':')[1].split('|')

        total = -1

        for n in numbers.split():
            if n in winners.split():
                total += 1
        if total >= 0:
            result += 2 ** total
    print(result)


if __name__ == '__main__':
    main()