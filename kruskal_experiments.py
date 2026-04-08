"""
@author: Radosław Pławecki
"""

from graph_utils import generate_graph, draw_graph_with_mst
from algorithms import kruskal
import statistics
import csv
import time

n_s = [1e3, 5e3, 1e4, 5e4, 1e5, 2.5e5, 5e5, 7.5e5, 1e6]  # for sparse
trials = 5

results = []

for n in n_s:
    n = int(n)
    # choose type of graph
    m = n  # sparse
    # m = 2 * n  # medium
    # m = n * (n - 1) // 2  # dense 
    times = []
    for _ in range(trials):
        edges = generate_graph(n, m)
        start = time.perf_counter()
        kruskal(n, edges)
        end = time.perf_counter()
        times.append(end - start)
    avg_time = statistics.mean(times)
    std_time = statistics.stdev(times)
    results.append([n, m, avg_time, std_time])
    print(f"n={n}, avg={avg_time:.5f}, std={std_time:.5f}")

with open("results/sparse.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter=';')
    header = ["$n$", "$m$", "$\overline t$", "$s$"]
    writer.writerow(header)
    writer.writerows(results)


# draw_graph_with_mst(n, edges, mst)
