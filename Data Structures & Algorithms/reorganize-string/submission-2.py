import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)

        n = len(s)

        maxFreq = max(freq.values())
        if maxFreq > (n + 1) // 2:
            return ""
        heap = [(count, char) for char, count in freq.items()]
        heapq.heapify_max(heap)

        res = []
        prev = (0, "")

        while heap:
            count, char = heapq.heappop_max(heap)
            res.append(char)

            count -= 1

            if prev[0] > 0:
                heapq.heappush_max(heap, prev)
            
            prev = (count, char)
        return "".join(res)

