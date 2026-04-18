import heapq
from collections import Counter

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heapq.heappush_max(heap, (a, "a"))
        if b > 0:
            heapq.heappush_max(heap, (b, "b"))
        if c > 0:
            heapq.heappush_max(heap, (c, "c"))
        
        res = ""

        while heap:
            count1, char1 = heapq.heappop_max(heap)

            if len(res) >= 2 and res[-1] == char1 and res[-2] == char1:
                if not heap:
                    break
                
                count2, char2 = heapq.heappop_max(heap)

                res += char2
                count2 -= 1

                if count2 > 0:
                    heapq.heappush_max(heap, (count2, char2))
                
                heapq.heappush_max(heap, (count1, char1))
            
            else:
                res += char1
                count1 -= 1

                if count1 > 0:
                    heapq.heappush_max(heap, (count1, char1))
        return res
        