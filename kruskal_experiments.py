"""
@author: Radosław Pławecki
"""

from graph_utils import generate_graph, draw_graph_with_mst
from algorithms import kruskal


n = 100
m = n * (n - 1) // 2
edges = generate_graph(n, m)
mst, weight = kruskal(n, edges)
# draw_graph_with_mst(n, edges, mst)
