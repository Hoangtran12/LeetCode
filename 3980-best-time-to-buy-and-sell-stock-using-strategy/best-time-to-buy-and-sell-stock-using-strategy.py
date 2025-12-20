class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        half_k = k // 2

        baseline_vals = [p * s for p, s in zip(prices, strategy)]
        prefix_sum = [0] + list(accumulate(baseline_vals))
        total_baseline = prefix_sum[n]

        current_sub_window_sum = sum(prices[half_k:k])
    
        original_window_val = prefix_sum[k] - prefix_sum[0]
        first_window_profit = total_baseline - original_window_val + current_sub_window_sum

        max_profit = max(total_baseline, first_window_profit)

        for i in range(1, n - k + 1):
            entering_val = prices[i + k - 1]
            leaving_val = prices[i + half_k - 1]
            current_sub_window_sum += entering_val - leaving_val

            original_window_val = prefix_sum[i + k] - prefix_sum[i]
            current_profit = total_baseline - original_window_val + current_sub_window_sum
            
            max_profit = max(max_profit, current_profit)

        return max_profit