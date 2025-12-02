import sys
import day06p01

def rotate(idx):
    coords = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    return coords[idx % 4]

def bfs(matrix, start_r, start_c):
    visited = set()
    stack = [(start_r, start_c, rotate(0), 0)]

    while stack:
        r, c, d, idx = stack.pop()

        if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]):
            return visited

        visited.add((r, c))
        print(r, c)

        nr, nc = r + d[0], c + d[1]
        if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]) and matrix[nr][nc] == '#':
            idx += 1
            d = rotate(idx)

        stack.append((r + d[0], c + d[1], d, idx))
    return visited

def main():
    matrix = [[char for char in line if char != '\n'] for line in sys.stdin]
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == '^':
                happy_path = day06p01.dfs(matrix, r, c,)
                break
    
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == '^':
                dfs(matrix, r, c,)
                break

if __name__ == '__main__':
    print(main())
