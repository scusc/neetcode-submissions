import heapq
from collections import defaultdict
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        pq = [(0, src, 0)]  # (cost, node, stops)

        # best[node][stops] = min cost to reach node with stops
        best = [[float('inf')] * (k + 2) for _ in range(n)]
        best[src][0] = 0

        while pq:
            cost, node, stops = heapq.heappop(pq)

            if node == dst:
                return cost

            if stops > k:
                continue

            for nei, price in graph[node]:
                newCost = cost + price
                if newCost < best[nei][stops + 1]:
                    best[nei][stops + 1] = newCost
                    heapq.heappush(pq, (newCost, nei, stops + 1))

        return -1

            


        