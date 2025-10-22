class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()

        f = collections.Counter(nums)

        mx = 0

        for i in nums:
            for j in [i, i-k, i+k]:
                left = bisect.bisect_left(nums, j-k)
                right = bisect.bisect_right(nums, j+k)
                count = right - left

                mx= max(mx, f[j] + min(numOperations, count - f[j]))
        
        return mx
        