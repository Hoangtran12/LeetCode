class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10 ** 9 + 7
        current_seats = 0
        current_plants = float('-inf')
        count = 1

        if corridor.count("S") % 2 != 0:
            return 0
        if "S" not in corridor:
            return 0
 
        for c in corridor:
            if c == "S":
                current_seats +=1

                if current_seats ==1:
                    if current_plants >=0:
                        count = (count * (current_plants + 1)) % MOD
                elif current_seats == 2:
                    current_seats = 0
                    current_plants = 0
            else:
                current_plants +=1
                
        return count % MOD