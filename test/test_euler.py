import unittest

from problems._001.euler_001 import *
from problems._002.euler_002 import *
from problems._003.euler_003 import *
from problems._004.euler_004 import *
from problems._005.euler_005 import *
from problems._006.euler_006 import *
from problems._007.euler_007 import *


class EulerTests(unittest.TestCase):
    def test_euler__1(self):
        self.assertEqual(sum3or5_naive(10), 23)
        self.assertEqual(sum3or5_list_comprehension(10), 23)
        self.assertEqual(sum3or5_naive(1000), 233168)
        self.assertEqual(sum3or5_list_comprehension(1000), 233168)

    def test_euler__2(self):
        self.assertEqual(sum_fib(4000000), 4613732)

    def test_euler__3(self):
        self.assertEqual(largest_prime(), 6857)

    def test_euler__4(self):
        self.assertEqual(test_for_palindromes(100, 100), 9009)
        self.assertEqual(test_for_palindromes(1000, 1000), 906609)

    def test_euler__5(self):
        self.assertEqual(divisible_by_range(2520, 1, 10), True)
        self.assertEqual(euler_005(), 232792560)

    def test_euler__6(self):
        self.assertEqual(sum_of_squares(10), 385)
        self.assertEqual(square_of_sum(10), 3025)
        self.assertEqual(difference_of_squares(10), 2640)
        self.assertEqual(difference_of_squares(100), 25164150)

    def test_euler__7(self):
        self.assertEqual(is_prime_num(5), True)
        self.assertEqual(is_prime_num(10), False)
        self.assertEqual(sieve_of_eratosthenes(1000000, 6), 13)
        self.assertEqual(sieve_of_eratosthenes(1000000, 10001), 104743)

if __name__ == '__main__':
    unittest.main()
