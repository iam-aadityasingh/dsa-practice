def missingNumber(self, nums: list[int]) -> int:
    n = len(nums)
    sum_n = n * (n + 1) // 2
    missing = sum_n - sum(nums)
    return missing