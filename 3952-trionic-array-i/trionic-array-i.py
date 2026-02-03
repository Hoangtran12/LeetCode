class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if len(nums) < 2: 
            return False
            
        if nums[0] >= nums[1]:
            return False

        segments = 1
        
        increasing = True
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return False
            
            if increasing:
                if nums[i] < nums[i-1]:
                    segments += 1
                    increasing = False
            else:
                if nums[i] > nums[i-1]:
                    segments += 1
                    increasing = True
            
            if segments > 3:
                return False

        return segments == 3