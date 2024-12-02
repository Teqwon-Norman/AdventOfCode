import sys

def is_safe(nums: list[str]) -> int:
    return all(nums[i-1] < nums[i] and 1 <= abs(nums[i] - nums[i - 1]) <= 3 for i in range(1, len(nums))) or \
        all(nums[i-1] > nums[i] and 1 <= abs(nums[i] - nums[i - 1]) <= 3 for i in range(1, len(nums)))

def main():
    ans = 0
    for line in sys.stdin:
        nums = list(map(int, line.split()))
        if is_safe(nums):
            ans += 1
    return ans

if __name__ == "__main__":
    print(main())
