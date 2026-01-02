class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if nums[i]==nums[j]:
                    return nums[i]
        return 0
        