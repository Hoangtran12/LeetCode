class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        spaces = k

        for n in nums:
            if n == 1:
                if spaces < k:
                    return False
                spaces = 0
            else:
                spaces +=1
        return True