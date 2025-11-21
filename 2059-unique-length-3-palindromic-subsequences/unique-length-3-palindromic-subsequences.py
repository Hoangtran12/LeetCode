class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        chars = set(s) 
        res = 0
        
        for c in chars:
            first = s.find(c)
            last = s.rfind(c)
            if last > first + 1:
                res += len(set(s[first + 1 : last]))
        return res