class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        foundX = foundY = foundZ = False

        for a,b,c in triplets:
            if a > x or b > y or c > z:
                continue
            
            if a == x:
                foundX = True
            
            if b == y:
                foundY = True
            
            if c == z:
                foundZ = True
        return foundX and foundY and foundZ