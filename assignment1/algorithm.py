#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import wraps
import time


class Utils(object):

    @staticmethod
    def execution_time(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            return_value = func(*args, **kwargs)
            message = "Executing {} took {:.10f} seconds.\n".format(func.__name__,
                                                                 time.time() - start)
            print(message)
            return return_value
        return wrapper

    @staticmethod
    def swap_by_index(x, a, b):
        assert( a >= 0 and b > a)
        t = x[a]
        x[a] = x[b]
        x[b] = t


    @staticmethod
    def swap(a, b):
        assert(type(a) == type(b))
        c = a
        a = b
        b = c
        return a, b


class Sort(object):

    @staticmethod
    def insertion_sort(list):
        """ Based on the pseudocode of page 18 of the Introduction to Algorithms book. """

        if not list:
            return None
        n = len(list)
        for i in range(0,n):
            cur = list[i]
            j = i
            while j > 0 and list[j-1] > cur:
                list[j] = list[j-1]
                j = j-1
            list[j] = cur
        return list

    @staticmethod
    def selection_sort(list):
        if not list:
            return None
        n = len(list)
        for i in range(0, n-1):
            min_ = i
            for j in range(i+1, n):
                if(list[j] < list[min_]):
                    min_ = j
            if min_ != i:
                list[i], list[min_] = Utils.swap(list[i], list[min_])
        return list
