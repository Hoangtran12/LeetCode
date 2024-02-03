class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0

        # checking if the number current stock is greater than previous, just add the difference
        for i in range(1,len(prices)):
            if (prices[i] > prices[i-1]):
                res += prices[i] - prices[i-1]
        return res       