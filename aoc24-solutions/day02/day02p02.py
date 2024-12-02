import sys
from day02p01 import is_safe

def main():
    ans = 0
    for line in sys.stdin:
        nums = list(map(int, line.split()))
        for i in range(len(nums)):
            if (is_safe(nums[:i] + nums[i+1:])):
                ans += 1
                break
    return ans

if __name__ == "__main__":
    print(main())
