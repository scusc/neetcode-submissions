class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = [[] for _ in range(n + 1)]

        def dfs(current, target, visited):
            if current == target:
                return True
            
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    if dfs(neighbor, target, visited):
                        return True
            return False

        for u, v in edges:
            if dfs(u, v, set()):
                return [u, v]
            graph[u].append(v)
            graph[v].append(u)
        
        return []