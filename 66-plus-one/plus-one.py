class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            nums = int(''.join(map(str, digits)))
            nums += 1
            digits_list = [int(digit) for digit in str(nums)]
            return digits_list



        