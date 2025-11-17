class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        ones_count = result = 0

        for c in s:
            if c == "1":
                ones_count +=1
                result += ones_count
            else:
                ones_count = 0
        return result % MOD