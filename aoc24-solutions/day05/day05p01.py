import sys
from collections import defaultdict
from itertools import pairwise

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


def main():
    data = sys.stdin.read().split()
    first, rules = builder(data)
    correct = []

    for r in rules:
        if all( b in first[a] for a, b in pairwise(r)):
            correct.append(r)
    print(sum(int(c[len(c) // 2]) for c in correct))
    print(correct)

if __name__ == '__main__':
    print(main())
