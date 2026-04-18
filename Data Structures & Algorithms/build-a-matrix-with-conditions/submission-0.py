class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topoSort(edges):
            indegrees = [0] * (k + 1)
            adj = [[] for _ in range(k + 1)]
            for src, dest in edges:
                adj[src].append(dest)
                indegrees[dest] += 1
            
            sortOrder = []
            q = deque()
            for i in range(1, k + 1):
                if not indegrees[i]:
                    q.append(i)
            
            while q:
                node = q.popleft()
                sortOrder.append(node)
                
                for nei in adj[node]:
                    indegrees[nei] -= 1
                    if not indegrees[nei]:
                        q.append(nei)
            
            return sortOrder
        
        rowOrder = topoSort(rowConditions)
        if len(rowOrder) != k:
            return []

        colOrder = topoSort(colConditions)
        if len(colOrder) != k:
            return []
        
        res = [[0] * k for _ in range(k)]

        colIndex = [0] * (k + 1)
        for i in range(k):
            colIndex[colOrder[i]] = i
        
        for i in range(k):
            res[i][colIndex[rowOrder[i]]] = rowOrder[i]
        
        return res



        