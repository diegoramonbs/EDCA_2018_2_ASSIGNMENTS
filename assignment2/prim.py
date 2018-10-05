#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from priority_queue import PriorityQueue

def prim(g, n):

    # Set initial condition for Prim algorithm
    parent = [None] * n
    toVisit = [True] * n

    pq = PriorityQueue()

    for u in range(n):
        if u == 0:
            pq.push([0, u])
        else:
            pq.push([sys.maxint, u])

    while not pq.empty():
        cost, u = pq.pop()
        toVisit[u] = False
        for v in range(0, n):
            if g[u][v] and toVisit[v] and g[u][v] < pq[v]:
                parent[v] = u
                pq.push([g[u][v], v])

    print("(origem, destino) -> custo")
    for i in range(1, n):
        print("({}, {}) -> {}".format(parent[i], i, g[i][parent[i]]))
    print("Custo total: {}".format(sum(g[i][parent[i]] for i in range(1, n))))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: prim.py [file]')
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename) as f:
        N, =  [int(x) for x in next(f).split()]
        graph = [[0]*N for i in range(N)]

        for line, i in zip(f, range(N)):
            for x, j in zip(line.split(), range(i+1, N)):
                graph[i][j] = int(x)
                graph[j][i] = int(x)

    prim(graph, N)
