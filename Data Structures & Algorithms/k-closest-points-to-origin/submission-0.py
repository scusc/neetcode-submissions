class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        heapq.heapify(maxHeap)

        for x, y in points:
            radiusFromCenter = -(x ** 2 + y ** 2)

            heapq.heappush(maxHeap, [radiusFromCenter, x, y])

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
            
        print(maxHeap)
        res = []
        while maxHeap:
            point = heapq.heappop(maxHeap)
            res.append([point[1], point[2]])            
        
        return res