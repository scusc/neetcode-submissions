import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        pq = [(0, src, 0)]  # (cost, node, stops)
        while pq:
            cost, node, stops = heapq.heappop(pq)
            if node == dst:
                return cost
            if stops <= k:
                for nei, price in graph[node]:
                    heapq.heappush(pq, (cost + price, nei, stops + 1))
        return -1