class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        low = min(nums)
        high = max(nums)
        counts = [0]*(high + 1 + k)
        for num in nums:
            counts[num] += 1
        in_range = 0
        res = 0
        for num in range(low, high + 1 + k):
            in_range += counts[num]
            if num > 2*k:
                in_range -= counts[num - 2*k - 1]
            if num > k:
                current = counts[num - k] + min(
                    numOperations,
                    in_range - counts[num - k]
                )
                res = max(res, current)
        return res