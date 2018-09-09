"""

Bynary search recurrence:

    T(n) = 1            , n = 1    (Initial condition)
         = c + T(n/2)   , n >= 2   (Recurrence relation)

Let n = 2^k (power of 2, n even) and Expading

    T(n) = c + T(n/2)
    T(n/2) = c + T(n/4)
    T(n) = c + c + T(n/4) = 2c + T(n/4)
    T(n/4) = c + T(n/8)
    T(n) = 2c + c + T(n/8) = 3c + T(n/8)
    T(n) = kc + T(n/2^k),

Let n/2^k = 1 => k = log2 n

Now,

    T(n) = c(log2 n) + T(n/(log2 n))
    T(n) = c(log2 n)+ T(1)

Therefore,

    T(n) = O(log2 n)

For any n (odd or even):

n is between two powers of 2, thus:

    2^k-1 <= n <= 2^k

Therefore,

    2^k-1 <= n => k <= log n + 1

and
    n <= 2^k => T(n) <= T(2^k) = c 2^k log2 k

    T(n) <= c k 2^k
         <= c(log n + 1) 2^(log n + 1)
         <= c(log n + 1) 2^log n 2
         <= 2 c n (log n + 1)
         <= c' n log n  + c'n

Applying the ratio theorem,

    lim (c' n log n  + c'n) / (n log n) as n -> inf = c'

Therefore, T(n) = O(log2 n) for any n.

"""


def bsearch(v, p, r, key):
    m = (p+r)//2

    if v[m] ==  key:
        return m
    if p >= r:
        return None
    else:
        if v[m] < key:
            return bsearch(v, m+1, r, key)
        else:
            return bsearch(v, p, m-1, key)

if __name__ == '__main__':
    v = [1,3,7,8,20,29,47,201,1204]
    r = bsearch(v, 0, len(v), 20)
    assert(r == 4)