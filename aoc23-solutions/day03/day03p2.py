import sys
from itertools import batched

def inbounds(r: int, c: int, grid: list[str]) -> bool:
    return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[r])

def parse_number(pair: tuple[int, ...], grid: list[str]):
    r, c = pair
    s = ''
    while c < len(grid[r]) and grid[r][c].isdigit():
        s += grid[r][c]
        c += 1
    return int(s)

def main() -> None:
    grid = sys.stdin.readlines()
    cs = set()
    total = 0

    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch.isdigit() or ch != "*":
                continue

            part_numbers: set[tuple[int, ...]] = set()

            for cr in [r-1, r, r+1]:
                for cc in [c-1, c, c+1]:
                    if not inbounds(cr, cc, grid) or not grid[cr][cc].isdigit():
                        continue
                    
                    while cc > 0 and grid[cr][cc-1].isdigit():
                        cc -= 1
                    
                    if part_numbers not in cs:
                        part_numbers.add((cr, cc))
            
            if len(part_numbers) == 2:
                x, y = part_numbers
                cs.add(x)
                cs.add(y)

                total += parse_number(x, grid) * parse_number(y, grid)
            
    print(total)
    
if __name__ == '__main__':
    main()
