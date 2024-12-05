import sys

def check(matrix, r, c):
    top_left = matrix[r - 1][c - 1]
    bottom_left = matrix[r + 1][c - 1]
    top_right = matrix[r - 1][c + 1]
    bottom_right = matrix[r + 1][c + 1]

    p1 = (top_left + matrix[r][c] + bottom_right)
    p2 = (top_right + matrix[r][c] + bottom_left)

    if p1 == 'MAS' and p2 == 'MAS' or p1 == 'SAM' and p2 == 'SAM' or \
        p1 == 'MAS' and p2 == 'SAM' or p1 == 'SAM' and p2 == 'MAS':
        return 1
    return 0

def main():
    matrix = [[char for char in line.rstrip()] for line in sys.stdin]

    count = 0
    for r in range(1, len(matrix) - 1):
        for c in range(1, len(matrix[0]) - 1):
            if matrix[r][c] == 'A':
                count += check(matrix, r, c)
    return count


if __name__ == '__main__':
    print(main())
