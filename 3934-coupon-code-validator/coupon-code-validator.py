class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        result = []
        lines = {"electronics", "grocery", "pharmacy", "restaurant"}
        for c, b, s in zip(code, businessLine, isActive):
            if not s:
                continue
            if b not in lines:
                continue
            if not c or not all(x.isalnum() or x == '_'for x in c):
                continue
            result.append((c, b))
        
        result.sort(key=lambda x: (x[1], x[0]))
        return [x[0] for x in result]