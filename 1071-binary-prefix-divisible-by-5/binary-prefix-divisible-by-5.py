class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        current = 0

        for num in nums:
            current = (current << 1) + num
            ans.append(current % 5 == 0)
        return ans