class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        freq = Counter(nums)
        # Zeros only interact with zeros
        zeros = freq[0]
        cnt = (zeros * (zeros - 1) * (zeros - 2) // 6) 
    
        prev = Counter()
        
        for x in nums:
            if x == 0:
                continue 
            x2 = x << 1
            if x2 in prev: # Small check to avoid lookup if not needed
                cnt += prev[x2] * (freq[x2] - prev[x2])           
            prev[x] += 1
            
        return cnt % MOD