class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        if n < 2:
            return 0
        
        if k >= n:
            return sum(abs(prices[i] - prices[i-1]) for i in range(1, n))

        x0 = prices[0]
        flat = [0] * (k + 1)
        longs = [-x0] * (k + 1)
        shorts = [x0] * (k + 1)

        for price in prices[1:]:
            for t in range(k, 0, -1):
                prev_closed = flat[t-1]

                flat[t] = max(flat[t], longs[t] + price, shorts[t] - price)

                longs[t] = max(longs[t], prev_closed - price)

                shorts[t] = max(shorts[t], prev_closed + price)

        return flat[k]