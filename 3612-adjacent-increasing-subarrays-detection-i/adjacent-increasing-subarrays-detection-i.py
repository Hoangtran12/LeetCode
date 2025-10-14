from typing import List

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if len(nums) == 0:
            return False

        # Step 1: Find the lengths of all consecutive increasing subarrays
        lengths = []
        count = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                count += 1
            else:
                lengths.append(count)
                count = 1
        lengths.append(count) # Add the last subarray length

        # Step 2: Check the conditions on the list of lengths
        # Check rule 1: Splitting a single subarray in half
        for l in lengths:
            if l // 2 >= k:
                return True

        # Check rule 2: Combining two adjacent subarrays
        for i in range(1, len(lengths)):
            l1 = lengths[i-1]
            l2 = lengths[i]
            if min(l1, l2) >= k:
                return True
        
        return False
