class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_appl = sum(apple)
        capacity.sort(reverse = True)

        count = 0
        while total_appl > 0:
            total_appl -= capacity[count]
            count += 1
        
        return count
