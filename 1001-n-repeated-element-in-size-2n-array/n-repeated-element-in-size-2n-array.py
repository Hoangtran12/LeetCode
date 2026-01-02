class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)

        for i in counts:
            if counts[i] > 1:
                return i