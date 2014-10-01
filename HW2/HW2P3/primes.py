import time

def find_primes(n):
    #Start the timer    
    start = time.time()
    ints = []
    #Only need a list of the odd numbers... we'll start with 3
    p = 3
    while p <= n:  
        ints.append(p)
        p += 2
    p = 2
    j = 0
    while p < n:
        #Add the current prime because it won't be caught by the checker (p mod p == 0)
        primes = [p]
        i = 0
        while i < len(ints):
            #If the current number mod p doesn't equal zero, then the current number
            #is not divisible by p and it could be a prime
            if ints[i]%p != 0:
                primes.append(ints[i])
                i += 1
            #If the current number is divisible by p, then it can't be prime
            else:
                i += 1
        #Set the list of primes for the current p to the working list to check the next p 
        ints = primes
        if j < len(primes) - 1:
            j += 1
            p = primes[j]
        #This just gets us out of the loop on the last iteration 
        else:
            p = n + 1
    #Stop the timer and save the time
    end = time.time()
    stopwatch = end - start
    return (primes,stopwatch)