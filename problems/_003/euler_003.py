import math


def largest_prime(n=600851475143):
    for i in range(2, int(math.sqrt(n))):
        if (n % i) == 0:
            n = n / i
            if n == 1 or n == i:
                return i
