class Solution:
    def uniquePaths(self, rows: int, cols: int) -> int:
        pathCounts = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows): pathCounts[r][0] = 1
        for c in range(cols): pathCounts[0][c] = 1

        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                pathCounts[r][c] = pathCounts[r - 1][c] + pathCounts[r][c - 1]
        
        return pathCounts[rows - 1][cols - 1]
        