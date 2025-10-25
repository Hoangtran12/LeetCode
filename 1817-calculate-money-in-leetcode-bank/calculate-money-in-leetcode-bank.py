class Solution:
    def totalMoney(self, n: int) -> int:
        result, monday = 0, 1

        while n > 0:
            for day in range (min(n, 7)):
                result += monday + day
            n -= 7
            monday +=1
        return result