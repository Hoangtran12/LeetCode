class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        lower_limit, upper_limit = -2**31, 2**31 - 1
        i = 0
        n = len(s)

        while i < n and s[i] == ' ':
            i+=1
        if i == n:
            return 0
        sign = 1
        if s[i] =='+':
            i+=1
        elif s[i] == '-':
            i+=1
            sign = -1
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            result = result * 10 + digit

            if sign * result <= lower_limit:
                return lower_limit
            if sign * result >= upper_limit:
                return upper_limit
            
            i += 1
        return result * sign


        