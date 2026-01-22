from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        ops = 0
        
        def is_non_dec():
            prev = -float('inf')
            for x in nums:
                if x is None: continue
                if x < prev: return False
                prev = x
            return True

        while not is_non_dec():
            min_pair_sum = float('inf')
            s = -1
            t = -1
            
            for i in range(n - 1):
                if nums[i] is None: continue
                
                j = i + 1
                while j < n and nums[j] is None:
                    j += 1
                
                if j < n:
                    pair_sum = nums[i] + nums[j]
                    if pair_sum < min_pair_sum:
                        min_pair_sum = pair_sum
                        s = i
                        t = j
            
            if s != -1:
                nums[s] += nums[t] 
                nums[t] = None
                ops += 1
            else:
                break
                
        return ops