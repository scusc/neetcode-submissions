class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        inDegrees = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                for dx, dy in directions:
                    nr, nc = r + dx, c + dy
                    if (0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] < matrix[r][c]):
                        inDegrees[r][c] += 1
        
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if inDegrees[r][c] == 0:
                    q.append((r, c, 1)) # (row, col, chain length)
                
        longestPath = 0

        while q:
            row, col, curLen = q.popleft()
            longestPath = max(longestPath, curLen)

            for dx, dy in directions:
                nx, ny = row + dx, col + dy
                if (0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] > matrix[row][col]):
                    inDegrees[nx][ny] -= 1
                    if inDegrees[nx][ny] == 0:
                        q.append((nx, ny, curLen + 1))
        
        return longestPath


