filename = "./reports.txt"


def is_safe(nums, limit=3):
    def inc(seq):
        return all(0 < seq[i + 1] - seq[i] <= limit for i in range(len(seq) - 1))

    def dec(seq):
        return all(0 < seq[i] - seq[i + 1] <= limit for i in range(len(seq) - 1))

    def passes(seq):
        return inc(seq) or dec(seq)

    if passes(nums):
        return True

    for k in range(len(nums)):
        if passes(nums[:k] + nums[k + 1 :]):
            return True
    return False


safe = 0
unsafe = 0
with open(filename, "r") as file:
    for line in file:
        nums = list(map(int, line.split()))
        if is_safe(nums, limit=3):
            safe += 1
        else:
            unsafe += 1

print("unsafe:", unsafe)
print("safe:", safe)
