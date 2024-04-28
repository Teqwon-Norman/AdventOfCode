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
    print(sum(add(symbol) for symbol in sys.stdin.read()))
    
if __name__ == "__main__":
    main()