class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edgeList = []

        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                edgeList.append((cost, i, j))
        
        edgeList.sort()

        parent = list(range(n))
        rank = [0] * n

        def findParent(child):
            if parent[child] != child:
                parent[child] = findParent(parent[child]) 
            return parent[child]

        def union(x, y):
            rootOfX = findParent(x)
            rootOfY = findParent(y)
            if rootOfX == rootOfY:
                return False # means cycle can be formed
            
            if rank[rootOfX] < rank[rootOfY]:
                parent[rootOfX] = rootOfY
            elif rank[rootOfX] > rank[rootOfY]:
                parent[rootOfY] = rootOfX
            else:
                parent[rootOfY] = rootOfX
                rank[rootOfX] += 1
            
            return True


        totalCost = 0
        edgesUsed = 0

        for cost, u, v in edgeList:
            if union(u,v):
                totalCost += cost
                edgesUsed += 1
                if edgesUsed == n - 1:
                    break
        return totalCost


        