class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        # sl = SortedList()
        p1, p2 = -1, -1
        count = 0
        for start, end in intervals:
            if start > p2:
                count +=2
                p1, p2 = end -1, end
            elif start > p1:
                count +=1
                p1, p2 = p2, end
        return count