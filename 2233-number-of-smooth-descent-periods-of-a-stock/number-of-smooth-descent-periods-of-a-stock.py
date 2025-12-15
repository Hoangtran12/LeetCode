class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        total, prev, current = 0, 0, 0

        for price in prices:
            if price + 1 == prev:
                current += 1
            else:
                current = 1
            prev = price
            total += current
    
        return total


        