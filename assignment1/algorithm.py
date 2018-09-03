#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Reference: Introduction to Algorithms - Thomas H. Cormen et al

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
    def insertion_sort(arr):
        if not arr:
            return None

        if len(arr) < 2:
            return arr

        n = len(arr)
        for i in range(0,n):
            cur = arr[i]
            j = i
            while j > 0 and arr[j-1] > cur:
                arr[j] = arr[j-1]
                j = j-1
            arr[j] = cur
        return arr

    @staticmethod
    def selection_sort(arr):
        if not arr:
            return None

        if len(arr) < 2:
            return arr

        n = len(arr)
        for i in range(0, n-1):
            min_ = i
            for j in range(i+1, n):
                if(arr[j] < arr[min_]):
                    min_ = j
            if min_ != i:
                arr[i], arr[min_] = arr[min_], arr[i]
        return arr


    @staticmethod
    def quick_sort(arr):
        if not arr:
            return None

        if len(arr) < 2:
            return arr

        def partition(arr, p, r):
            x = arr[r]
            i = p - 1
            for j in range(p, r):
                if arr[j] <= x:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i+1], arr[r] = arr[r], arr[i+1]
            return i+1

        def recursive(arr, p, r):
            if p < r:
                q = partition(arr, p, r)
                recursive(arr, p, q-1)
                recursive(arr, q+1, r)

        recursive(arr, 0, len(arr)-1)
        return arr

    @staticmethod
    def merge_sort(list):
        def recursive(list):
            if len(list)>1:
                mid = len(list)//2
                lefthalf = list[:mid]
                righthalf = list[mid:]

                recursive(lefthalf)
                recursive(righthalf)

                i, j, k = 0, 0, 0

                while i < len(lefthalf) and j < len(righthalf):
                    if lefthalf[i] < righthalf[j]:
                        list[k]=lefthalf[i]
                        i=i+1
                    else:
                        list[k]=righthalf[j]
                        j=j+1
                    k=k+1

                while i < len(lefthalf):
                    list[k]=lefthalf[i]
                    i=i+1
                    k=k+1

                while j < len(righthalf):
                    list[k]=righthalf[j]
                    j=j+1
                    k=k+1
            return list

        if not list:
            return None
        return recursive(list)