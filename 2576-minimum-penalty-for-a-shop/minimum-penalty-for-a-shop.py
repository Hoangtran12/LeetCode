class Solution:
    def bestClosingTime(self, customers: str) -> int:

        x = y = z = 0
        
        for i, s in enumerate(customers):
            z += 1 if s == "Y" else -1
            if z > y:
                y, x = z, i + 1 
                
        return x
                