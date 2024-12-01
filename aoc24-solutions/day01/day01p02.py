import sys
from collections import Counter

def get_score(l1, freq) -> int:
    total = 0
    for num in l1:
        total += (num * freq[num])
    return total

def main():
    l1, l2 = [], []
    for line in sys.stdin:
        a, b = line.split()
        l1.append(int(a))
        l2.append(int(b))
    return get_score(l1, Counter(l2))

if __name__ == '__main__':
    print(main())
