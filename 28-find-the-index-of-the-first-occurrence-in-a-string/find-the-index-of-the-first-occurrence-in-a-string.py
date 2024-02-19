class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        x = len(needle)
        for i in range(len(haystack)):
            if needle == haystack[i:i+x]:
                return i
        return -1        