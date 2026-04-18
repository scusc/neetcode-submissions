from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dest in sorted(tickets, reverse = True):
            adj[src].append(dest)
        
        stack = []

        def dfs(airport):
            while adj[airport]:
                nextDest = adj[airport].pop()
                dfs(nextDest)
            
            stack.append(airport)
        
        dfs("JFK")
        return stack[::-1]
        