import sys
from collections import defaultdict
from itertools import pairwise
from functools import cmp_to_key

def builder(data):
    f = defaultdict(set)
    r = []

    for sub in data:
        if '|' in sub:
            a, b = sub.split('|')
            f[a].add(b)

        elif sub == '\n':
            continue

        else:
            r.append(sub.split(','))
    return f, r

def cmp_factory(first):
    def cmp(x, y):
        if x in first[y]:
            return -1
        elif y in first[x]:
            return 1
        else:
            return 0
    return cmp

def main():
    data = sys.stdin.read().split()
    first, rules = builder(data)
    correct = []

    for r in rules:
        if not all( b in first[a] for a, b in pairwise(r)):
            cmp = cmp_factory(first)
            x = sorted(r, key=cmp_to_key(cmp))
            correct.append(x)
    print(sum(int(c[len(c) // 2]) for c in correct))

if __name__ == '__main__':
    print(main())
