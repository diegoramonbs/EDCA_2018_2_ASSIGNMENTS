#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from priority_queue import PriorityQueue

def dijkstra(g, n, origin=0):

    # Set initial condition for dijkstra algorithm
    toVisit = [True] * n
    dist = [sys.maxint] * n

    pq = PriorityQueue()

    for u in range(n):
        if u == origin:
            pq.push([0, u])
        else:
            pq.push([sys.maxint, u])

    while not pq.empty():
        cost, u = pq.pop()
        toVisit[u] = False
        for v in range(0, n):
            if g[u][v] != 0 and toVisit[v] and cost + g[u][v] < pq[v]:
                pq.push([g[u][v] + cost, v])
                dist[v] = pq[v]

    print("(origem, destino) -> custo")
    for i in range(1, n):
        print("({}, {}) -> {}".format(origin, i, dist[i]))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: dijkstra.py [file]')
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename) as f:
        N, =  [int(x) for x in next(f).split()]
        graph = [[0]*N for i in range(N)]

        for line, i in zip(f, range(N)):
            for x, j in zip(line.split(), range(i+1, N)):
                graph[i][j] = int(x)
                graph[j][i] = int(x)

    dijkstra(graph, N)
