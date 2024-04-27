import sys

def vowel_check(s: str) -> bool:
    count: int = 0
    for ch in s:
        if ch in 'aeiou':
            count += 1
    return count >= 3

def has_forbidden_pair(s: str) -> bool:
    for pair in ['ab', 'cd', 'pq', 'xy']:
        if pair in s:
            return True
    return False

def has_double_chars(s: str) -> bool:
    if has_forbidden_pair(s):
        return False

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            return True
    return False
    
def main() -> None:
    total: int = 0

    for line in sys.stdin.readlines():
        string = line.rstrip()
        if vowel_check(string) and has_double_chars(string):
            total += 1
    print(total)

if __name__ == "__main__":
    main()
