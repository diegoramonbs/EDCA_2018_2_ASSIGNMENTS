#!/usr/bin/python
# -*- coding: utf-8 -*-


# Implementar uma solução de Programação Dinâmica para  problema do caixeiro viajante.
# Entrada:
#           N   -> |V|
#           dij -> função distâncias dos arcos(Matriz de Adjacência)
#
# Exemplo de entrada:
# 4
# 0 23 17 19
# 14 0 22 20
# 23 15 0 25
# 13 19 21 0

import math
import sys
import itertools
import time

# Traveling Salesman Problem(TSP)
class TSP:
    """ Solve the Traveling Salesman Problem.
        The constructor receives as input an adjacency
        matrix (Graph) containing the weights and the
        number of rows and columns of the matrix (N). """
    def __init__(self, graph, N):
        self.graph = graph
        self.N = N

    def run(self):

        if self.N <= 20:
            # Bit number required to represent all possibile sets
            self.npow = int(math.pow(2, self.N))

            # g(i, S) is length of shortest path starting at i
            # visiting all vertices in S ending at 1
            self.g = [[-1]*self.npow for _ in range(self.N)]
            self.p = [[-1]*self.npow for _ in range(self.N)]
            self.d = graph
            self.output = []

            # g(i, {}) direct edge between (i, 1)
            for i in range(0, self.N):
                self.g[i][0] = graph[i][0]

            # npow - 2 to exclude the current vertex
            result = self._eval1(0, self.npow - 2)

            self.output.append(1)
            self._path(0, self.npow - 2)
            self.output.append(result)
            return self.output
        else:
            print('Implementation only supports n <= 20, otherwise, memory error occurs.')
            sys.exit(1)

    def _path(self, start, Set):
        # Stop condition, reached null set
        if self.p[start][Set] == -1:
            return

        cur = self.p[start][Set]
        mask = self.npow - 1 - int(math.pow(2, cur))
        # Remove cur from set
        masked = Set & mask
        self.output.append(cur+1)
        self._path(cur, masked)

    def _eval1(self, start, Set):

        """ To represent the sets we used bit bitmasking For example, the mask 10000101
            means that he subset[1...8] consists of elements 1, 3 and 8. A set of N elements
            there are total 2^N subsets thus 2^N masks are possible, one representing
            each subset. Each mask is in fact an integer number written in binary notation """

        # Result represents the minimum cost
        masked, mask, result = -1, -1, -1

        # Memoization DP top-down: If the sub-problem
        # has already been resolved,return your previously
        # calculated solution.
        if self.g[start][Set] != -1:
            return self.g[start][Set]
        else:
            for cur in range(0, self.N):
                # Remove current vertex from this set( Exclude the base vertex from set)
                mask = self.npow - 1 - int(math.pow(2, cur))
                # print (masked, "{0:b}".format(mask))
                masked = Set & mask
                if masked != Set:
                    # Eval the removed set
                    # best[subset][end] = min(best[subset \ { end }][i] + dist[i][end])
                    tmp = self.d[start][cur] + self._eval1(cur, masked)
                    # If the sub-problem has not been resolved or the
                    # current value is the minimum value
                    if result == -1 or result > tmp:
                        # Removing the current vertex gave the minimum cost
                        result = tmp
                        self.p[start][Set] = cur
        self.g[start][Set] = result
        # Return the minimum cost
        return result

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: salesman.py [file]')
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename) as f:
        N, =  [int(x) for x in next(f).split()]
        graph = [[int(x) for x in line.split()] for line in f]

    start_time = time.time()
    result = TSP(graph, N).run()
    print("Executin dynamic programming TSP took {:.10f} seconds.".format(time.time() - start_time))

    print('instância: {0}'.format(filename))
    print('valor: {0}'.format(result[-1]))
    print('circuito: {0}'.format(result[:-1]))


















