import sys
import heapq as hq

def main() -> None:
    data: list[str] = sys.stdin.readlines()
    
    total: int = 0
    for line in data:
        equation: list[str] = line.rstrip().split('x')
        l, w, h = map(int, equation)
        heap: list[int] = [l+l, w+w, h+h]
        hq.heapify(heap)

        area = l * w * h
        total += (hq.heappop(heap) + hq.heappop(heap)) + area
    print(total)

if __name__ == "__main__":
    main()