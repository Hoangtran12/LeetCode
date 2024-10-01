class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        nums = int(''.join(map(str, digits)))
        nums += 1
        digits_list = [int(digit) for digit in str(nums)]

        return digits_list



        