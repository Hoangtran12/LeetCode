class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n  # Handle base cases

        cs = [0] * (n + 1)
        cs[0], cs[1] = 1, 1  # Base cases

        for i in range(2, n + 1):
            cs[i] = cs[i - 1] + cs[i - 2]  # Sum of the two previous steps

        return cs[n]  # Return the number of ways to reach the nth step
