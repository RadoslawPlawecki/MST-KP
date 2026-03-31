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


def draw_graph_with_mst(n, edges, mst):
    use_latex()
    G = nx.Graph()
    G.add_weighted_edges_from(edges)
    pos = nx.spring_layout(G)  
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    ax1 = axes[0]
    nx.draw(G, pos, with_labels=True, ax=ax1, node_color='lightblue')
    nx.draw_networkx_edge_labels(
        G, pos,
        edge_labels=nx.get_edge_attributes(G, 'weight'),
        ax=ax1
    )
    ax1.set_title("Pełny graf")
    ax2 = axes[1]
    MST = nx.Graph()
    MST.add_weighted_edges_from(mst)
    nx.draw(MST, pos, with_labels=True, ax=ax2,
            node_color='lightblue', edge_color='red', width=2)
    nx.draw_networkx_edge_labels(
        MST, pos,
        edge_labels=nx.get_edge_attributes(MST, 'weight'),
        ax=ax2
    )
    ax2.set_title("Minimalne drzewo spinające")
    plt.tight_layout()
    plt.show()
