class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        for i, n in enumerate(nums):
            if n % 2 == 0:
                nums[i] = -1
            else:
                nums[i] = n - (((n + 1) & -(n + 1)) >> 1)
        return nums
            