"""
@author: Radosław Pławecki
"""

import random
import networkx as nx
import matplotlib.pyplot as plt
from plot_formatting import use_latex


def generate_graph(n, m):
    edges = []
    used = set()
    for i in range(1, n):
        u = i
        v = random.randint(0, i - 1)
        w = random.randint(1, 100)
        edges.append((u, v, w))
        used.add((min(u, v), max(u, v)))
    while len(edges) < m:
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u == v:
            continue
        edge = (min(u, v), max(u, v))
        if edge in used:
            continue
        used.add(edge)
        w = random.randint(1, 100)
        edges.append((u, v, w))
    return edges


def build_adj_list(n, edges):
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    return adj


def build_matrix(n, edges):
    INF = float('inf')
    mat = [[INF] * n for _ in range(n)]
    for u, v, w in edges:
        mat[u][v] = w
        mat[v][u] = w
    return mat

