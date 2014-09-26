import numpy as np
import time

def find_primes(n):
    start = time.time()
    p = 2
    ints = np.linspace(p, n, num=n-1)
    j = 0
    while p < n:
        primes = [p]
        i = 0
        while i < len(ints):
            if ints[i]%p != 0:
                primes.append(ints[i])
                i += 1
            else:
                i += 1
        ints = primes
        if j < len(primes) - 1:
            j += 1
            p = primes[j]
        else:
            p = n + 1
    end = time.time()
    stopwatch = end - start
    return (primes,stopwatch)