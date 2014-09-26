from primes import find_primes

n = input('How high should we find primes?')

(primes,time) = find_primes(n)
print len(primes), 'prime numbers less than', n, 'found in', time, 'seconds!'
print primes