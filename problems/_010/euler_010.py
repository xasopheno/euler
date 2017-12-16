def euler_010(maximum):
    maximum += 1
    sum = 0
    cache = [True] * maximum
    cache[0] = cache[1] = False

    for (i, is_prime) in enumerate(cache):
        if i == maximum - 1:
            return sum
        if is_prime:
            sum += i

            for n in range(i*i, maximum, i):     # Mark factors non-prime
                cache[n] = False

