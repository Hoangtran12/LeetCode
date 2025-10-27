class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        count = [row.count("1") for row in bank if "1" in row]
        total = 0

        for p, c in zip(count, count[1:]):
            total += p*c
        return total