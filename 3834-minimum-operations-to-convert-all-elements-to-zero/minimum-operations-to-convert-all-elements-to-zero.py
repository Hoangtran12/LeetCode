class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        stack = [0]

        for x in nums:
            while len(stack) > 0:
                if x > stack[-1]:
                    count +=1
                    stack.append(x)
                    break
                elif x == stack[-1]:
                    break
                elif x < stack[-1]:
                    stack.pop()
        
        return count

        