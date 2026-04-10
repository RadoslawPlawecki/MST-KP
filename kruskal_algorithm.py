"""
@author:
"""

from union_find import UnionFind


class KruskalAlgorithm:
    def __init__(self, n):
        self.n = n

    def run_edge_list(self, edges):
        edges = edges.copy()
        edges.sort(key=lambda x: x[2])
        uf = UnionFind(self.n)
        mst = []
        total = 0
        for u, v, w in edges:
            if uf.union(u, v):
                mst.append((u, v, w))
                total += w
        return mst, total

    def run_adj_list(self, adj):
        edges = []
        for u in range(self.n):
            for v, w in adj[u]:
                if u < v:
                    edges.append((u, v, w))
        return self.run_edge_list(edges)

    def run_matrix(self, mat):
        INF = float('inf')
        edges = []
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if mat[i][j] != INF:
                    edges.append((i, j, mat[i][j]))
        return self.run_edge_list(edges)
