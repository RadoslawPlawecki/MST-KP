"""
@author: Radosław Pławecki
"""

from union_find import UnionFind
from graph_utils import draw_graph_with_mst
import heapq


def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    mst = []
    total_weight = 0
    for u, v, w in edges:
        if uf.union(u, v):  
            mst.append((u, v, w))
            total_weight += w
    return mst, total_weight


def prim(n, edges):
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    visited = [False] * n
    mst = []
    total_weight = 0
    heap = [(0, 0, -1)] 
    while heap and len(mst) < n - 1:
        w, u, parent = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        if parent != -1:
            mst.append((parent, u, w))
            total_weight += w
        for v, weight in graph[u]:
            if not visited[v]:
                heapq.heappush(heap, (weight, v, u))
    return mst, total_weight
