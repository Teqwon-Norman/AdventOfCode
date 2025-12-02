import sys

def solve(nums):
    back = len(nums) - 1

    while True:
        id = None
        from_indices = []
        to_indices = []

        while back >= 0:
            item = nums[back]
            if item != '.' and (id is None or id == item):
                id = item
                from_indices.append(back)
                back -= 1
            elif item == '.' and len(from_indices) == 0:
                back -= 1
            else:
                break

        front = 0

        while front <= back:
            item = nums[front]
            if item == '.':
                to_indices.append(front)
                if len(to_indices) == len(from_indices):
                    for a, b in zip(from_indices, to_indices):
                        nums[a], nums[b] = nums[b], nums[a]
                    break
            else:
                to_indices = []
            front += 1

        if back < 0:
            break

    return sum(idx * num if num != '.' else 0 for idx, num in enumerate(nums))

def main():
    data = sys.stdin.read().strip()
    count = 0
    nums = []

    for idx, char in enumerate(data):
        if idx % 2 == 0:
            nums += [count] * int(char)
            count += 1
        else:
            num = int(char)
            nums += ['.'] * num

    print(solve(nums))

main()
