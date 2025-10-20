class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s = set(nums)
        result = k

        while result in s:
            result +=k
        return result
        