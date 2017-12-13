import math

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?


def is_prime_num(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


def sieve_of_eratosthenes(max, goal):
    count = 0
    cache = [True] * max
    cache[0] = cache[1] = False

    for (i, is_prime) in enumerate(cache):
        if is_prime:
            count += 1
            if count == goal:
                return i
            for n in range(i*i, max, i):     # Mark factors non-prime
                    cache[n] = False
