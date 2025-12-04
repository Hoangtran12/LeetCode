class Solution:
    def countCollisions(self, directions: str) -> int:
        count = directions.count("L") + directions.count("R")

        for c in directions:
            if c != "L":
                break
            count -=1
        
        for c in reversed(directions):
            if c != "R":
                break
            count -=1

        return count