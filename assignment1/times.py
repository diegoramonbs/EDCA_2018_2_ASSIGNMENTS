#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Diego

from algorithm import Sort, Utils
import random


if __name__ == '__main__':

    # Initialize the random generator
    random.seed(None)

    # Length of List
    n = 10**4

    # Larger integer in list
    max_value = random.randint(0, n*2)

    # List with n random elements
    data = [ random.randint(0 ,max_value) for _ in range(0, n)]

    print("List with {} elements and with integers in the range [0,{}]\n".format(n, max_value))

    # Link to the decorator used in the measurement of the runtime function.
    isort_timed = Utils.execution_time(Sort.insertion_sort)
    ssort_timed = Utils.execution_time(Sort.selection_sort)
    qsort_timed = Utils.execution_time(Sort.quick_sort)
    msort_timed = Utils.execution_time(Sort.merge_sort)

    # Executes the algorithms.
    isort_timed(data)
    ssort_timed(data)
    qsort_timed(data)
    msort_timed(data)



