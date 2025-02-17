import sys

def multiply(a, b):
    return 2 * a * b

def main() -> None:
    data: list[str] = sys.stdin.readlines()
    
    total: int = 0
    for line in data:
        dimensions = line.rstrip().split('x')
        l, w, h = map(int, dimensions)
        total += multiply(l, w) + multiply(w, h) + multiply(h, l) + min(l * w, w * h, h * l)
    print(total)

if __name__ == "__main__":
    main()
