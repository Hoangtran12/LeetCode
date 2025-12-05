class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        left, count = 0, 0
        right = sum(nums)

        for num in nums[:-1]:
            left += num
            right -= num
            if abs(left - right) % 2 == 0:
                count +=1
        return count