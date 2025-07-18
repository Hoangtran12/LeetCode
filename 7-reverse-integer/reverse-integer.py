class Solution:
    def reverse(self, x: int) -> int:
        lower_limit, upper_limit = -2**31, 2**31 - 1
        sign = -1 if x < 0 else 1
        reversed_str = str(abs(x))[::-1]
        reversed_num = sign * int(reversed_str)

        if reversed_num < lower_limit or reversed_num > upper_limit:
            return 0

        return reversed_num



          
        