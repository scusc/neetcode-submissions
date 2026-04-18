import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minHeap = [(grid[0][0], 0, 0)] #(elevationTime, row, col)
        heapq.heapify(minHeap)
        
        visited = set((0, 0))
        maxTime = 0

        while minHeap:
            elevationTime, row, col = heapq.heappop(minHeap)

            maxTime = max(maxTime, elevationTime)

            if row == n - 1 and col == n - 1:
                return maxTime
            
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = row + dx, col + dy

                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    heapq.heappush(minHeap, (grid[nx][ny], nx, ny))
            
        return -1

        