class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 !=0:
            return False
        stack = []
        bracket = {'(' : ')', '{' : '}', '[' : ']'}

        for c in s:
            if c=='(' or c=='{' or c=='[':
                stack.append(c)
            elif not stack or bracket[stack.pop()]!=c:
                return False
        return not stack
