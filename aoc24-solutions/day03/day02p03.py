import sys
import re

def main():
    data = sys.stdin.read().replace('\n', '')
    sub_strings = re.sub(r"don't\(\).*?do\(\)", '', data)

    return sum (
        int(a) * int(b)
        for a, b in re.findall(r"mul\((\d+),(\d+)\)", sub_strings)
    )

if __name__ == '__main__':
    print(main())
