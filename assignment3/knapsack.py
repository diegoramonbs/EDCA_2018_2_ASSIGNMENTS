#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def knapsack(items, size):
    n = len(items)
    W = [[0] * (size + 1) for _ in range(n + 1)]

    for i, (w, v) in enumerate(items):
        i += 1
        for c in range(size + 1):
            if w > c:
                W[i][c] = W[i-1][c]
            else:
                W[i][c] = max(W[i-1][c], W[i-1][c-w]+v)


    i, j, p = n, size, []

    while i > 0:
        if W[i][j] != W[i-1][j]:
            p.append(i)
            j -= items[i-1][0]
        i -= 1

    return W[n][size], sorted(p)



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: knapsack.py [file]')
        sys.exit(1)

    header = True

    filename = sys.argv[1]

    with open(filename) as file:
        items = []
        for line in file:
            w, v = map(int, line.split())
            if header:
                n, size = w, v
                header = False
            else:
                items.append((w, v))

    g, p = knapsack(items, size)

    p = str(p).strip('[]')

    print('instância: {0}'.format(filename))
    print('valor: {0}'.format(g))
    print('produtos escolhidos: {0}'.format(p))