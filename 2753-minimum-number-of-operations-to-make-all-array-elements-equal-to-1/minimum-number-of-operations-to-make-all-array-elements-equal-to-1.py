class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        def gcd(a, b):
            while a and b:
                a = a % b
                b, a = a, b
            return max(a, b)
        
        ones= nums.count(1)

        if ones: return n - ones

        result = math.inf

        for l in range(n):
            num = 0
            for r in range(l, n):
                num = gcd(num, nums[r])
                if num == 1 : 
                    result = min(result, r - l)
                    break
        
        if result == math.inf: return -1
        return result + n -1
        