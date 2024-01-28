class Solution(object):
    def maximumDifference(self, nums):
        curr_min = nums[0]
        ans = 0
        
        for i in nums:
            if i < curr_min:
                curr_min = i
                
            ans = max(ans, i-curr_min)
            
        return -1 if ans == 0 else ans 
        