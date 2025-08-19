filename = "./reports.txt"


def is_safe(nums, limit=3):
    inc = all(nums[i] < nums[i + 1] for i in range(len(nums) - 1))
    dec = all(nums[i] > nums[i + 1] for i in range(len(nums) - 1))
    safe = inc or dec
    threshold = all(abs(nums[i + 1] - nums[i]) <= limit for i in range(len(nums) - 1))
    return safe and threshold


safe = 0
unsafe = 0

with open(filename, "r") as file:
    for line in file:
        nums = list(map(int, line.split()))
        if is_safe(nums, limit=3):
            safe += 1
        else:
            unsafe += 1


print(unsafe)
print(safe)
