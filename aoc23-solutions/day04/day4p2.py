import sys

def main() -> None:
    cards: list[str] = sys.stdin.readlines()
    scratchcard_count: list[int] = [ 1 for _ in range(len(cards)) ]

    for card_number, line in enumerate(cards):
        winners, numbers = line.split(':')[1].split('|')
        win_count: int = 0

        for n in numbers.split():
            if n in winners.split():
                win_count += 1
                scratchcard_count[card_number + win_count] += (scratchcard_count[card_number])
    print(sum(scratchcard_count))

if __name__ == '__main__':
    main()
