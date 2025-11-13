class Solution:
    def maxOperations(self, s: str) -> int:
        n= len(s)
        ones_count = 0
        result = 0

        for i in range(n):
            if s[i] == "1":
                ones_count +=1
            elif s[i] == "0" and s[i-1] == "1":
                result += ones_count
        return result