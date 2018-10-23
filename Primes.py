import time
from math import sqrt

i = 3
primes = [1,2]
start = time.time()
count = 1000000
while i < count:
    prime = True
    for prime in primes[1:]:
        if i % prime == 0:
            prime = False
            break
        if prime > sqrt(i):
            break

    if prime:
        primes.append(i)

    i += 2

print(time.time() - start)
    
