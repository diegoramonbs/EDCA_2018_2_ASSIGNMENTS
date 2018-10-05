#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from disjoint_set import DisjointSet
from operator import itemgetter

def kurskal(g, n):

    # Set initial condition for Kurskal algorithm
    mst = []

    ds = DisjointSet(n)

    edges = []

    for u in range(n):
        for v in range(u+1, n):
            if u != v:
                edges.append((u, v, g[u][v]))

    # Sort tuples (u, v, cost) by cost
    edges.sort(key=itemgetter(2))

    for u, v, c in edges:
        if ds.find(u) != ds.find(v):
            mst.append((u, v, c))
            ds.union(u, v)

    total_cost = 0
    print("(origem, destino) -> custo")
    for u, v, c in mst:
        total_cost += c
        print("({}, {}) -> {}".format(u, v, c))

    print("Custo total: {}".format(total_cost))



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: kurskal.py [file]')
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename) as f:
        N, =  [int(x) for x in next(f).split()]
        graph = [[0]*N for i in range(N)]

        for line, i in zip(f, range(N)):
            for x, j in zip(line.split(), range(i+1, N)):
                graph[i][j] = int(x)
                graph[j][i] = int(x)

    kurskal(graph, N)
