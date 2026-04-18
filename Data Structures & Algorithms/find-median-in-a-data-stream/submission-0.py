import heapq
class MedianFinder:

    def __init__(self):
        self.median = None
        self.lower = [] # max heap
        self.upper = [] # min heap
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.lower, -num)
        heapq.heappush(self.upper, -heapq.heappop(self.lower))

        if len(self.upper) > len(self.lower):
            heapq.heappush(self.lower, -heapq.heappop(self.upper))
        
        self.updateMedian()
    
    def updateMedian(self):
        if len(self.lower) > len(self.upper):
            self.median = float(-self.lower[0])
        
        else:
            maxLower = -self.lower[0]
            minUpper = self.upper[0]
            self.median = (maxLower + minUpper) / 2.0 

    def findMedian(self) -> float:
        return self.median
        
        