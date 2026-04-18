from typing import List

class Solution:
    def unionMerge(self, v1, v2, unions, unionMappings):
        if len(unions[unionMappings[v1]]) <= len(unions[unionMappings[v2]]):
            smallerUnion = unionMappings[v1]
            biggerUnion = unionMappings[v2]
        else:
            smallerUnion = unionMappings[v2]
            biggerUnion = unionMappings[v1]
        
        for v in unions[smallerUnion]:
            unions[biggerUnion].append(v)
            unionMappings[v] = biggerUnion
        
        del unions[smallerUnion]


    def kruskal(self, n, edges, skipEdge=None, forceEdge=None):

        unions = {v: [v] for v in range(n)}
        unionMappings = {v: v for v in range(n)}

        weight = 0
        edgesUsed = 0

        if forceEdge is not None:
            v1, v2, w, idx = edges[forceEdge]
            if unionMappings[v1] != unionMappings[v2]:
                self.unionMerge(v1, v2, unions, unionMappings)
                weight += w
                edgesUsed += 1

        for i, (v1, v2, w, idx) in enumerate(edges):

            if i == skipEdge:
                continue

            if unionMappings[v1] != unionMappings[v2]:
                self.unionMerge(v1, v2, unions, unionMappings)
                weight += w
                edgesUsed += 1

        if edgesUsed != n - 1:
            return float('inf')

        return weight


    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        edgeList = []

        for i, (src, dest, weight) in enumerate(edges):
            edgeList.append((src, dest, weight, i))

        sortedEdges = sorted(edgeList, key=lambda x: x[2])

        mstWeight = self.kruskal(n, sortedEdges)

        critical = []
        pseudo = []

        for i in range(len(sortedEdges)):

            if self.kruskal(n, sortedEdges, skipEdge=i) > mstWeight:
                critical.append(sortedEdges[i][3])

            elif self.kruskal(n, sortedEdges, forceEdge=i) == mstWeight:
                pseudo.append(sortedEdges[i][3])

        return [critical, pseudo]