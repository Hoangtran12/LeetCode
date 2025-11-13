class Solution:
    def maxOperations(self, s: str) -> int:
        n= len(s)
        zero_segments = 0
        result = 0

        for i in reversed(range(n)):
            if s[i] == "0":
                if (i == n - 1 or s[i+1] == "1"):
                    zero_segments +=1
            else:
                result += zero_segments
        return result