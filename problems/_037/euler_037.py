import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from helpers.sieve_of_eratosthenes import sieve_of_eratosthenes


class TruncatablePrimes:
    def __init__(self):
        self.primes = sieve_of_eratosthenes(10000000)

    def truncate_test(self, value):
        test = str(value)
        for i in range(len(test)):
            if not self.primes[int(test)]:
                return False
            test = test[1:]

        test = str(value)
        for i in range(len(test)):
            if not self.primes[int(test)]:
                return False
            test = test[:-1]
        return True


tp = TruncatablePrimes()


def euler_037():
    truncatable_primes = []
    for i in range(11, 1000000):
        if tp.truncate_test(i):
            print(i)
            truncatable_primes.append(i)
            if len(truncatable_primes) == 11:
                return sum(truncatable_primes)

