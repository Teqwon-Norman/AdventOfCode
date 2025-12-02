import sys

def main():
    data = sys.stdin.read().strip()
    count = 0
    nums = []

    for idx, char in enumerate(data):
        if idx % 2 == 0:
            nums += [count] * int(char)
            count += 1
        else:
            nums += ['.'] * int(char)

    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] == '.':
            nums[right], nums[left] = nums[left], nums[right]
            right -= 1

        while nums[right] == '.':
            right -= 1
        left += 1

    print(sum(
        idx * num if num != '.' else 0
        for idx, num in enumerate(nums)
    ))

if __name__ == '__main__':
    main()
