class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s2)
        dp = [0] * (m + 1)

        for c1 in s1:
            current_row = [0] * (m + 1)
            for j, c2 in enumerate(s2):
                if c1 == c2:
                    current_row[j + 1] = dp[j] + ord(c1)
                else:
                    current_row[j + 1] = max(dp[j + 1], current_row[j])
            
            dp = current_row

        total_ascii = sum(map(ord, s1 + s2))
        return total_ascii - 2 * dp[-1]