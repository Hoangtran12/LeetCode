class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        count, prev = 0, -math.inf
        for num in nums:
            if max(num - k, prev + 1) <= num + k:
                prev = max(num - k, prev + 1)
                count += 1
        return count