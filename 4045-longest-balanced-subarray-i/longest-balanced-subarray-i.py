class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        
        for i in range(n):
            if n - i <= max_len:
                break
                
            seen = set()
            balance = 0
            
            for j in range(i, n):
                val = nums[j]
                
                if val not in seen:
                    seen.add(val)
                    if val % 2 == 0:
                        balance += 1
                    else:
                        balance -= 1
                
                if balance == 0:
                    current_len = j - i + 1
                    if current_len > max_len:
                        max_len = current_len
                        
        return max_len