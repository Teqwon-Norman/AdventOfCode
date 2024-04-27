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

"""
Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without overlapping, 
like xyxy (xy) or aabcdefgaa (aa), 
but not like aaa (aa, but it overlaps).

It contains at least one letter which repeats with exactly one letter between them, 
like xyx, abcdefeghi (efe), or even aaa.
"""