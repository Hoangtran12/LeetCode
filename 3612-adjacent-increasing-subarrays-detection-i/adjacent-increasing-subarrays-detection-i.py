class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        count, precount, ans = 1, 0, 0

        for i in range (1, n):
            if nums[i] > nums[i-1]:
                count +=1
            else:
                precount, count = count, 1
            ans = max(ans, min(count, precount))
            ans = max(ans, count //2)
        
        return ans >= k

