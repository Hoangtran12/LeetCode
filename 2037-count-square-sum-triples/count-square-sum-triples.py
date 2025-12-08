class Solution:
    def countTriples(self, n: int) -> int:
        res = 0

        for a in range (1, n+1):
            for b in range (a+1, n+1):
                c_sq = (a*a + b*b)
                c = int(c_sq ** 0.5)
                if c > n: break
                if c * c == c_sq:
                    res +=2

        return res

