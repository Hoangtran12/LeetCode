class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
            
        i = 2
        while i**2 <= x:
            i += 1
        return i-1

        