import sys

def out_of_bounds(matrix, r, c):
    return r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0])

def dfs(matrix, r, c, curr, target, visited):
    if out_of_bounds(matrix, r, c) or matrix[r][c] != curr:
        return 0

    if matrix[r][c] == target:
        return 1


    count = (
            dfs(matrix, r + 1, c, curr + 1, target, visited) +
            dfs(matrix, r - 1, c, curr + 1, target, visited) +
            dfs(matrix, r, c + 1, curr + 1, target, visited) +
            dfs(matrix, r, c - 1, curr + 1, target, visited))
    return count

def main():
    matrix = [ [int(char) for char in line.strip()] for line in sys.stdin ]
    res = 0

    for r, _ in enumerate(matrix):
        for c, _ in enumerate(matrix[0]):
            if matrix[r][c] == 0:
                res += dfs(matrix, r, c, 0, 9, set())
    return res

if __name__ == '__main__':
    print(main())
