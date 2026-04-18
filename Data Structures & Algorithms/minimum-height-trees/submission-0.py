class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
    
        edgeCount = {}
        q = deque()

        for src, connections in adj.items():
            edgeCount[src] = len(connections)
            if len(connections) == 1:
                q.append(src)
        
        while q:
            if n <= 2:
                return list(q)
            
            for _ in range(len(q)):
                node = q.popleft()
                n -= 1
                for nei in adj[node]:
                    edgeCount[nei] -= 1
                    if edgeCount[nei] == 1:
                        q.append(nei)



                        