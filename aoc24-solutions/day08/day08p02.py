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
                
                x, y = a, b
                while 0 <= x + row < len(matrix) and 0 <= y + col < len(matrix[0]):
                    x += row
                    y += col
                    antinodes.add((x, y))

                x, y = c, d
                while 0 <= x + (-row) < len(matrix) and 0 <= y + (-col) < len(matrix[0]):
                    x += (-row)
                    y += (-col)
                    antinodes.add((x, y))
            antinodes.add((a, b))
            antinodes.add((c, d))
    print(len(antinodes))
    
if __name__ == '__main__':
    main()
