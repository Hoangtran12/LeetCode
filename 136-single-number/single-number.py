class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0

        for x in nums:
            a ^= x
        
        return a
        