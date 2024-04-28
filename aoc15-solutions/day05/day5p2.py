import sys

def contains_pairs(s: str) -> bool:
    seen: set = set()
    for i in range(len(s)-1):
        if s[i:i+2] in s[i+2:]:
            return True
    return False

def contains_palindrome(s: str) -> bool:
    for i in range(len(s)-2):
        if s[i] == s[i+2]:
            return True
    return False

def main() -> None:
    total: int = 0

    for line in sys.stdin.readlines():
        string = line.rstrip()
        if contains_pairs(string) and contains_palindrome(string):
            total += 1
    print(total)
        

if __name__ == "__main__":
    main()