import sys
import re

def main():
    return sum(
        int(a) * int(b)
        for line in sys.stdin
        for a, b in re.findall(r"mul\((\d+),(\d+)\)", line)
    )

if __name__ == '__main__':
    print(main())
