import sys

def dfs(matrix, r, c, idx, dr, dc, target):
    if idx == len(target):
        return 1

    if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]) or matrix[r][c] != target[idx]:
        return 0

    return dfs(matrix, r + dr, c + dc, idx + 1, dr, dc, target)

def main():
    matrix = [[char for char in line.rstrip()] for line in sys.stdin]

    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1)
    ]

    count = 0
    for r, _ in enumerate(matrix):
        for c, _ in enumerate(matrix[0]):
            if matrix[r][c] == 'X':
                for dr, dc in directions:
                    count += dfs(matrix, r, c, 0, dr, dc, "XMAS")
    return count


if __name__ == '__main__':
    print(main())
