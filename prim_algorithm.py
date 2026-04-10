"""
@author: Radosław Pławecki
"""

import heapq

class PrimAlgorithm:
    def __init__(self, n):
        self.n = n

    def run_adj_list(self, adj):
        visited = [False] * self.n
        heap = [(0, 0, -1)]
        mst = []
        total = 0
        while heap and len(mst) < self.n - 1:
            w, u, parent = heapq.heappop(heap)
            if visited[u]:
                continue
            visited[u] = True
            if parent != -1:
                mst.append((parent, u, w))
                total += w
            for v, weight in adj[u]:
                if not visited[v]:
                    heapq.heappush(heap, (weight, v, u))
        return mst, total

    def run_edge_list(self, edges):
        adj = [[] for _ in range(self.n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        return self.run_adj_list(adj)

    def run_matrix(self, mat):
        INF = float('inf')
        adj = [[] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                if mat[i][j] != INF:
                    adj[i].append((j, mat[i][j]))
        return self.run_adj_list(adj)
        