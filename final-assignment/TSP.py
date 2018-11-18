#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import sys
import time

def print_matrix(g):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
        for row in g]))

def read_graph(filename):
    """ Reads the graph from disk. """
    try:
        with open(filename) as f:
            N, =  [int(x) for x in next(f).split()]
            graph = [[int(x) for x in line.split()] for line in f]

        # Discard the time windows
        return graph[:N], N
    except IOError as ex:
        print("I/O error({0}): {1}".format(ex.errno, ex.strerror))
    except:
        print("Unexpected error:", sys.exc_info()[0])



def fn(cycle, graph):
    """ Compute the objetive function (cost of hamilton cycle)
        of travelling salesman problem. """

    total_cost = 0
    for i in range(len(cycle)-1):
        u, v = cycle[i], cycle[i+1]
        total_cost += graph[u][v]

    total_cost += graph[cycle[-1]][0]
    return total_cost

def build_random(size):
    """ Define a cycle initialised randomly. """
    cycle = range(1, size)
    random.shuffle(cycle)
    cycle.insert(0, 0)
    return cycle

def build_nearest_neighbour(graph, size):
    """ Define a cycle initialised using nearest neighbour approch. """

    cycle = [0] * size
    cur, next = 0, -1

    for k in range(1, size):
        min_cost = sys.maxsize
        for v in range(1, size):
            if graph[cur][v] < min_cost and graph[cur][v] > 0 and v not in cycle:
                min_cost = graph[cur][v]
                next = v
        cycle[k] = next
        cur = next
    return cycle


def two_opt(cycle, graph, debug=True):
	""" 2-opt local search. """

	best = cycle
	improved = True
	n = len(cycle)

	while improved:
	    improved = False
	    for i in range(1, n-2):
	        for j in range(i+1, n):
	            if j-i == 1:
	                continue
	            new_cycle = cycle[:]
	            new_cycle[i:j] = cycle[j-1:i-1:-1]

	            if fn(new_cycle, graph) < fn(cycle, graph):
	                best = new_cycle
	                improved = True

	    if debug:
	        print("[2-opt] -> cycle cost reduced from {} to {}".format(fn(cycle, graph), fn(best, graph))) 
	    cycle = best
	return best

def one_shift(cycle, graph, debug=True):
	""" 1-shift local search. """

	best = cycle
	improved = True
	n = len(cycle)
	while improved:
	    improved = False
	    for i in range(1, n-2):
	        for j in range(i+1, n):
	            if j-i == 1:
	                continue
	            new_cycle = cycle[:]
	            new_cycle[i], new_cycle[j] = new_cycle[j], new_cycle[i]
	            for k in range(i, j-1):
	                t = new_cycle[k] 
	                new_cycle[k] = new_cycle[k+1]
	                new_cycle[k+1] = t
	            if fn(new_cycle, graph) < fn(cycle, graph):
	                best = new_cycle
	                improved = True
	    if debug:
	        print("[1-shift] -> cycle cost reduced from {} to {}".format(fn(cycle, graph), fn(best, graph)))       
	    cycle = best
	return best


def perturbation(cycle, graph, k, debug):
	n = len(cycle)
	t = cycle[:]
	for _ in range(k): 
	    i = random.randint(1, n-1)
	    j = random.randint(1, n-1)
	    cycle[i], cycle[j] = cycle[j], cycle[i]
	if debug:
		print('[Perturbation] -> cycle cost from {} to {}'.format(fn(t, graph), fn(cycle, graph)))

	return cycle

def local_search(cycle, graph, debug=True):
    best = cycle
    improved = True
    n = len(cycle)

    while improved:
        new_cycle = one_shift(cycle, graph, debug)
        new_cycle = two_opt(new_cycle, graph, debug)       
        if fn(new_cycle, graph) < fn(cycle, graph):
            best = new_cycle
            improved = True
        else:
        	improved = False     
        cycle = best
    return best



def VNS(g, N, Kmax, debug=False):
	k = 1 
	x = build_nearest_neighbour(g, N)
	best = x

	while k < Kmax:
	    t = perturbation(best, g, k, debug)
	    t = local_search(best, g, debug)

	    if fn(t, g) < fn(best, g):
	    	best = t 
	        k = 1
	    else:
	    	k += 1

	return best, fn(best, g)


#g, N = read_graph("data/professor/pcv10.txt")

#print(VNS(g, N, 3, True))

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('Usage: TSP.py [file]')
		sys.exit(1)

	g, N = read_graph(sys.argv[1])

	start_time = time.time()
	cycle, cost = VNS(g, N, 2, False)
	print("Executin VNS took {:.10f} seconds.".format(time.time() - start_time))
	print('cycle: {}'.format(cycle))
	print('cost: {}'.format(cost))

