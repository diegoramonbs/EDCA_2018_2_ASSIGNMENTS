#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from algorithm import Sort, Utils


def to_output(list):
    for elem in list:
        print("{}".format(elem))


def get(arg,data):
    options = {
        1: Sort.insertion_sort,
        2: Sort.selection_sort,
        3: Sort.quick_sort,
        4: Sort.merge_sort,
        5: Sort.counting_sort,
        6: sorted
    }
    algorithm = options.get(arg)
    #timed = Utils.execution_time(algorithm)
    return algorithm(data)

if __name__ == '__main__':
    first = True
    choice = int(sys.argv[1])

    assert( choice >= 1 and choice <= 6)

    for line in enumerate(sys.stdin):
        if first:
            data = [None]*int(line[1])
            first = False
        else:
            data[line[0]-1] = int(line[1])

    ordered = []
    ordered = get(choice, data)
    to_output(ordered)

