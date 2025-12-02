import sys

def is_calibrated(target, curr_total, nums, idx=0):
    if idx == len(nums):
        return target == curr_total

    return (is_calibrated(target, curr_total * nums[idx], nums, idx + 1) or
            is_calibrated(target, curr_total + nums[idx], nums, idx + 1))

def main():
    return sum(
        int(parts[0])
        for line in sys.stdin
        for parts in [line.strip().split(':')]
        if is_calibrated(
            int(parts[0]),
            int(parts[1].split()[0]),
            list(map(int, parts[1].split()[1:]))
        )
    )

if __name__ == "__main__":
    print(main())
