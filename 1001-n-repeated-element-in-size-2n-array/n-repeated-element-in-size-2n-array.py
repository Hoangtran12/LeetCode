class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()

        for i in nums:
            if i in seen:
                return i
            seen.add(i)
        
        return -1