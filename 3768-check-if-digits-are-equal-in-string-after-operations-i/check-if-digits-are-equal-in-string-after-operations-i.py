class Solution:
    def hasSameDigits(self, s: str) -> bool:
        i = 0
        new_s = ""

        while len(s) > 2 and i < len(s) - 1:
            new_s += str((int(s[i]) + int(s[i+1])) % 10)
            i += 1

            if i == len(s) - 1:
                s = new_s
                i = 0
                new_s = ""
        return len(s) == 2 and s[0] == s[1]        