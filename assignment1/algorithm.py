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
    def merge_sort(arr):
        def recursive(arr):
            if len(arr)>1:
                m = len(arr)//2
                L = arr[:m]
                R = arr[m:]

                recursive(L)
                recursive(R)

                i, j, k = 0, 0, 0

                while i < len(L) and j < len(R):
                    if L[i] < R[j]:
                        arr[k]=L[i]
                        i=i+1
                    else:
                        arr[k]=R[j]
                        j=j+1
                    k=k+1

                while i < len(L):
                    arr[k]=L[i]
                    i=i+1
                    k=k+1

                while j < len(R):
                    arr[k]=R[j]
                    j=j+1
                    k=k+1
            return arr

        if not arr:
            return None
        if len(arr) < 2:
            return arr
        return recursive(arr)


    @staticmethod
    def counting_sort(arr):
        if not arr:
            return None

        if len(arr) < 2:
            return arr

        length = len(arr)
        largest = max(arr)+1
        count = [0] * largest
        output = [None] * length

        for i in arr:
            count[i] += 1

        for i in range(1, largest):
            count[i] += count[i-1]

        for i in reversed(range(0, length)):
            output[count[arr[i]]-1] = arr[i]
            count[arr[i]] -= 1

        return output

    @staticmethod
    def radix_sort(arr):
        def counting_sort_radix(arr, k):
            if not arr:
                return None

            if len(arr) < 2:
                return arr

            length = len(arr)
            largest = max(arr)+1
            count = [0] * largest
            output = [None] * length

            for i in arr:
                count[(i/k)%10] += 1

            for i in range(1, largest):
                count[i] += count[i-1]

            for i in reversed(range(0, length)):
                output[count[ (arr[i]/k)%10]-1] = arr[i]
                count[(arr[i]/k)%10] -= 1

            return output

        m = max(arr)
        k = 1
        while m/k > 0:
            arr = counting_sort_radix(arr, k)
            k *= 10
        return arr

    @staticmethod
    def bucket_sort(arr):
        pass