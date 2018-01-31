from problems.helpers.sieve_of_eratosthenes import sieve_of_eratosthenes


def rotate(n):
    n = str(n)
    return n[1:]+n[:1]


def check_rotations(n, primes):
    for x in range(2, n):
        n = rotate(n)
        if not primes[int(n)]:
            return False
    return True


def circular_primes(n):
    count = 0
    primes = sieve_of_eratosthenes(n)
    for x in reversed(range(2, len(primes))):
        if check_rotations(x, primes):
            count += 1

    return count

