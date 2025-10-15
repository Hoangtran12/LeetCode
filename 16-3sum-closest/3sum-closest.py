class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        min_diff, closest_sum = float('inf'), float('inf')

        for i in range (n-2):
            left, right = i+1, n-1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                current_diff = abs(current_sum - target)

                if current_diff < min_diff:
                    min_diff, closest_sum = current_diff, current_sum
                    
                if current_sum < target:
                    left +=1
                else:
                    right -=1

        return closest_sum


                


