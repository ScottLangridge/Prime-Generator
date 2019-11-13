from math import sqrt


i = 3
primes = [1,2]
count = 30

while i < count:
    is_prime = True
    for prime in primes[1:]:
        if i % prime == 0:
            break
        if prime > sqrt(i):
            primes.append(i)
            break
    i += 2

print(primes)
