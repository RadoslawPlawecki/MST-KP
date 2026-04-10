"""
@author: Radosław Pławecki
"""

from graph_utils import generate_graph, build_adj_list, build_matrix
from kruskal_algorithm import KruskalAlgorithm
from prim_algorithm import PrimAlgorithm
from tqdm import tqdm
import statistics
import csv
import time


# analysing algorithms effectiveness
"""n_s = [1e3, 5e3, 1e4, 5e4, 1e5, 2.5e5, 5e5, 7.5e5, 1e6]  # for sparse
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
    writer.writerows(results)"""


# analysing different graph representation
n_s = [250, 500, 750, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
trials = 100

results = []

for n in n_s:
    n = int(n)
    m = 2 * n
    kr_times = []
    pr_times = []
    for _ in tqdm(range(trials)):
        edges = generate_graph(n, m)
        adj = build_adj_list(n, edges)
        mat = build_matrix(n, edges)
        kr = KruskalAlgorithm(n)
        pr = PrimAlgorithm(n)
        # kruskal
        t0 = time.perf_counter()
        kr.run_matrix(mat)
        t1 = time.perf_counter()
        kr_times.append(t1 - t0)
        # prim
        t0 = time.perf_counter()
        pr.run_matrix(mat)
        t1 = time.perf_counter()
        pr_times.append(t1 - t0)

    results.append([
        n,
        m,
        statistics.mean(kr_times),
        statistics.stdev(kr_times),
        statistics.mean(pr_times),
        statistics.stdev(pr_times)
    ])

with open("results/mat.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["n", "m", "kr_mean", "kr_std", "prim_mean", "prim_std"])
    writer.writerows(results)
