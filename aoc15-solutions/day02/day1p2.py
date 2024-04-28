import sys

def main() -> None:
    data: list[str] = sys.stdin.readlines()
    
    total: int = 0
    for line in data:
        dimensions = line.rstrip().split('x')
        l, w, h = map(int, dimensions)
        total += (2 * l * w) + (2 * w * h) + (2 * h * l) + min(l * w, w * h, h * l)
    print(total)

if __name__ == "__main__":
    main()