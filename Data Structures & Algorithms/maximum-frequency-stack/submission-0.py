from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.heap = []
        self.count = defaultdict(int)
        self.index = 0
        
    def push(self, val: int) -> None:
        self.count[val] += 1
        heapq.heappush_max(self.heap, (self.count[val], self.index, val))        
        self.index += 1

    def pop(self) -> int:
        _, _, val = heapq.heappop_max(self.heap)
        self.count[val] -= 1
        return val        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()