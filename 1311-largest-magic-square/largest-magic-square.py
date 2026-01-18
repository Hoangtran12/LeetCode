class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        row_prefix = [list(accumulate(row, initial=0)) for row in grid]
        col_prefix = [list(accumulate(col, initial=0)) for col in zip(*grid)]

        diag = [[0] * (C + 1) for _ in range(R + 1)]
        anti_diag = [[0] * (C + 1) for _ in range(R + 1)]

        for r in range(R):
            for c in range(C):
                val = grid[r][c]
                diag[r + 1][c + 1] = diag[r][c] + val
                anti_diag[r + 1][c] = anti_diag[r][c + 1] + val

        def is_magic_square(r, c, k):
            target = diag[r + k][c + k] - diag[r][c]
            anti_val = anti_diag[r + k][c] - anti_diag[r][c + k]
            if target != anti_val:
                return False

            for i in range(k):
                row_sum = row_prefix[r + i][c + k] - row_prefix[r + i][c]
                if row_sum != target:
                    return False
                col_sum = col_prefix[c + i][r + k] - col_prefix[c + i][r]
                if col_sum != target:
                    return False
                    
            return True

        max_possible_k = min(R, C)
        for k in range(max_possible_k, 1, -1):
            for r in range(R - k + 1):
                for c in range(C - k + 1):
                    if is_magic_square(r, c, k):
                        return k
                        
        return 1