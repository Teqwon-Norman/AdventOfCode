import sys
from collections import defaultdict

def main():
    matrix = [ [char for char in line.strip()] for line in sys.stdin ]
    freq = defaultdict(list)
    antinodes = set()

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            char = matrix[r][c]
            if char.isalnum():
                freq[char].append((r, c))

    for v in freq.values():
        for first in range(len(v)):
            for second in range(first + 1, len(v)):
                a, b = v[first]
                c, d = v[second]
                row, col = a-c, b-d

                if 0 <= a + row < len(matrix) and 0 <= b + col < len(matrix[0]):
                    antinodes.add((a + row, b + col))

                if 0 <= c + (-row) < len(matrix) and 0 <= d + (-col) < len(matrix[0]):
                    antinodes.add((c + (-row), d + (-col)))

    print(len(antinodes))
if __name__ == '__main__':
    main()
