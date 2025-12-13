class Solution:
    def validateCoupons(self, codes: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        priority = {
            "electronics": 0, 
            "grocery": 1, 
            "pharmacy": 2, 
            "restaurant": 3
        }
        groups = [[] for _ in range(4)]
        
        for code, line, active in zip(codes, businessLine, isActive):
            if not active or line not in priority:
                continue
            
            cleaned = code.replace('_', '')
            if code and (cleaned == "" or cleaned.isalnum()):
                groups[priority[line]].append(code)
        
        result = []
        for group in groups:
            result.extend(sorted(group))
            
        return result