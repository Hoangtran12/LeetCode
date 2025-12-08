class Solution:
    def countOdds(self, low: int, high: int) -> int:
        def f(x):
            return (x+1) // 2
        return f(high) - f(low - 1)