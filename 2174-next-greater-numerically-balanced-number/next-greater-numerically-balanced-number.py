class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        return p[bisect.bisect_right(p, n)]

p = []

def good(x):
    f = collections.Counter(str(x))

    for k, v in f.items():
        if int(k) != v:
            return False
    return True

for x in range (1, 1000000):
    if good(x):
        p.append(x)
p.append(1224444)