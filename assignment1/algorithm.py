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
        return b, a

class Heap(object):
    def __init__(self, data):
        self.data = data
        self.size = len(data)

        self.build()

    def build(self):
        for i in range(self.size//2, -1, -1):
            self._heapify(i)

    def _heapify(self, i):
        left = 2*i+1
        right = 2*i+2
        largest = i

        if left < self.size and self.data[left] > self.data[i]:
            largest = left
        else:
            largest = i
        if right < self.size and self.data[right] > self.data[largest]:
            largest = right
        if largest != i:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            self._heapify(largest)

    def pop(self):
        ret = self.data[0]
        del self.data[0]
        self._heapify(0)
        return ret

    def top(self):
        return self.data[0]

    def sort(self):
        for i in range(self.size-1, -1, -1):
             self.data[0], self.data[i] = self.data[i], self.data[0]
             self.size -= 1
             self._heapify(0)
        return self.data

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
    def bucket_sort(arr, num_bucket=10):
        if not arr:
            return arr

        bucket = [[] for b in range(num_bucket)]
        output = []

        for i in range(len(arr)):
            bucket[int(arr[i] * num_bucket)].append(arr[i])

        for i in range(num_bucket):
            Sort.insertion_sort(bucket[i])

        for i in range(num_bucket):
            if bucket[i]:
                output += bucket[i]

        return output


    @staticmethod
    def heap_sort(arr):
        if not arr:
            return None
        if len(arr) < 2:
            return arr

        heap = Heap(arr)
        return heap.sort()

