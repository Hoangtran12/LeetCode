class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        
        row_sums = [sum(row) for row in mat]
        col_sums = [sum(mat[r][c] for r in range(m)) for c in range(n)]
        
        count = 0
        
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1 and row_sums[r] == 1 and col_sums[c] == 1:
                    count += 1
                    
        return count