import sys

def inbounds(r: int, c: int, grid: list[str]) -> bool:
    return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[r])

def main() -> None:
    grid: list[str] = sys.stdin.readlines()
    start_of_number_indexes: set = set()

    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch.isdigit() or ch == ".":
                continue

            for cr in [r-1, r, r+1]:
                for cc in [c-1, c, c+1]:
                    if not inbounds(cr, cc, grid) or not grid[cr][cc].isdigit():
                        continue
                    
                    while cc > 0 and grid[cr][cc-1].isdigit():
                        cc -= 1
                    
                    start_of_number_indexes.add((cr, cc))
    
    res = []

    for r, c in start_of_number_indexes:
        s = ''
        while c < len(grid[r]) and grid[r][c].isdigit():
            s += grid[r][c]
            c += 1
        res.append(int(s))
    print(sum(res))
    
if __name__ == '__main__':
    main()
