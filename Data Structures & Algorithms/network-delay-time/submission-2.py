from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for src, dest, time in times:
            edges[src].append((dest, time))
        
        minHeap = [(0, k)] #time, node -> order important because minHeap will be done based on time.
        visited = set()
        resTime = 0
        heapq.heapify(minHeap)
        
        while minHeap:
            time, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            
            visited.add(node)
            resTime = time

            for neiDest, neiTime in edges[node]:
                if neiDest not in visited:
                    heapq.heappush(minHeap, (time + neiTime, neiDest))
            
        
        return resTime if len(visited) == n else -1
