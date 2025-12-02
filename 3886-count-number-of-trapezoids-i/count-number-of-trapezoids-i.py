class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        y_counts = Counter(y for x, y in points)
        segment_counts = []

        for count in y_counts.values():
            if count >= 2:
                segments = count * (count - 1) // 2
                segment_counts.append(segments)

        total_segments = sum(segment_counts)
        res = 0

        for current_level_segments in segment_counts:
            total_segments -= current_level_segments
            res += current_level_segments * total_segments

        return res % MOD