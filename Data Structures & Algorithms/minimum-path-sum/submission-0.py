class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    dp[r][c] = grid[r][c]
                
                elif r == 0:
                    dp[r][c] = grid[r][c] + dp[r][c - 1]
                
                elif c == 0:
                    dp[r][c] = grid[r][c] + dp[r - 1][c] 
                
                else:
                    dp[r][c] = grid[r][c] + min(dp[r - 1][c], dp[r][c - 1])

        return dp[rows - 1][cols - 1]
        