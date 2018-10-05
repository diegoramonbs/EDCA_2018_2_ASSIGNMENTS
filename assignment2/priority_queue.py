#!/usr/bin/python
# -*- coding: utf-8 -*-


class PriorityQueue(object):
    def __init__(self, heap = None):
        if not heap:
            heap = []
        self.heap = heap

        self._build()

    @staticmethod
    def _parent(i):
        return (i-1)/2

    @staticmethod
    def _left(i):
        return 2*i+1

    @staticmethod
    def _right(i):
        return 2*i+2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify(self, i):
        l = self._left(i)
        r = self._right(i)
        largest = i

        if l < len(self.heap) and self.heap[l] < self.heap[i]:
            largest = l
        else:
            largest = i
        if r < len(self.heap) and self.heap[r] < self.heap[largest]:
            largest = r
        if largest != i:
            self._swap(i, largest)
            self._heapify(largest)

    def _build(self):
        for i in range(len(self.heap)//2, -1, -1):
            self._heapify(i)

    def pop(self):
        if len(self.heap) == 1:
            return self.heap.pop()
        elem = self.heap[0]
        self.heap[0] = self.heap.pop(-1)
        self._heapify(0)
        return elem

    def _decrease_key(self, i):
       while i:
            parent = self._parent(i)
            if self.heap[parent] < self.heap[i]:
                break
            self._swap(i, parent)
            i = parent

    def push(self, value):
        n = len(self.heap)
        for v in range(1,n-2):
            if self.heap[v][1] == value[1]:
                del self.heap[v]
        self.heap.append(value)
        self._decrease_key(len(self.heap)-1)

    def peek(self):
        return self.heap[0]

    def empty(self):
        return len(self.heap) == 0

    def __str__(self):
        return str(self.heap)


    def __getitem__(self, key):
        for v in range(len(self.heap)):
            if self.heap[v][1] == key:
                return self.heap[v][0]



if __name__ == '__main__':
    pq = PriorityQueue()

    pq.push([3, 'a'])
    pq.push([12,'h'])
    pq.push([1,'b'])
    pq.push([2,'c'])

    print(pq)

    pq.push([0, 'h'])

    print(pq)

