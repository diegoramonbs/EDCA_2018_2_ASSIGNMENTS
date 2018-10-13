#!/usr/bin/python
# -*- coding: utf-8 -*-

def fib1(n):
    if n < 2:
        result = 1
    else:
        result = fib1(n-1) + fib1(n-2)
    return result

def fib2(n, memo={}):
    if n in memo:
        return memo[n]
    if n < 2:
        result = 1
    else:
        result = fib2(n-1, memo) + fib2(n-2, memo)
    memo[n] = result
    return result

def fib3(n):
    if n == 1 or n == 2:
        return 1
    T = [None] * (n+1)
    T[1] = 1
    T[2] = 1
    for i in range(3, n+1):
        T[i] = T[i-1] + T[i-2]
    return T[n]
