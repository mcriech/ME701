from primes import find_primes

n = input('How high should we find primes?')

(primes,time) = find_primes(n)
print '\n', len(primes), 'prime numbers less than', n, 'found in', time, 'seconds!\n'
print primes