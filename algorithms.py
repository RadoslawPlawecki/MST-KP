"""
@author: Radosław Pławecki
"""

from union_find import UnionFind
from graph_utils import draw_graph_with_mst


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
