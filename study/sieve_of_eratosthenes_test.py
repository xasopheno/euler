import math
import time

def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    for mult_of_two in range(4, n + 1, 2):
        primes[mult_of_two] = False

    for j in range(3, int(math.sqrt(n)) + 1, 2):
        if primes[j]:
            for k in range(j * j, n + 1, j):
                primes[k] = False

    return primes

sieve = sieve_of_eratosthenes(10000000)
counter = 0
for value in sieve:
    if sieve[counter]:
        print(counter)
    else:
        print('.')
    # print(counter, sieve[counter])
    counter += 1
    time.sleep(0.01)
