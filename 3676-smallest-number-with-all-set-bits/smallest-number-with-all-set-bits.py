class Solution:
    def smallestNumber(self, n: int) -> int:
        result = 1
        while result < n: 
            result = result * 2 + 1
        return result