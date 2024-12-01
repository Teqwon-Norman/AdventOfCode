import sys
import heapq as heap


def get_distance(h1, h2) -> int:
    total = 0
    for _ in range(len(h1)):
        a = heap.heappop(h1)
        b = heap.heappop(h2)
        total += abs(a - b)
    return total


def main():
    h1, h2 = [], []
    for line in sys.stdin:
        a, b = line.split()
        heap.heappush(h1, int(a))
        heap.heappush(h2, int(b))
    return get_distance(h1, h2)

if __name__ == '__main__':
    print(main())
