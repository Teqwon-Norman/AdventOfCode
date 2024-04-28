import sys


def add(symbol: str) -> int:
    match(symbol):
        case '(':
            return 1
        case ')':
            return -1
        case default:
            raise ValueError(f"Invalid symbol: {symbol}")


def main() -> None:
    res: int = 0
    for idx, symbol in enumerate(sys.stdin.read()):
        res += add(symbol)

        if res == -1:
            print(idx + 1)
            break
    
if __name__ == "__main__":
    main()