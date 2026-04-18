from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.pointsCounts = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.pointsCounts[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        
        px, py = point

        for x, y in self.points:

            # check if the current iteration point is a diagonal or not, we need this to be diagonal.
            # and also points should not be stacked on top of each other.
            if (abs(px - x) != abs(py - y)) or x == px or y == py:
                continue
            
            res += self.pointsCounts[(x, py)] * self.pointsCounts[(px, y)]
        
        return res
            



        
