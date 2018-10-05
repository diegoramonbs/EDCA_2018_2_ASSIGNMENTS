#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def knapsack(items, size):
    pass



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

    knapsack(items, size)


