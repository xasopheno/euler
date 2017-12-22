import unittest

from problems._001.euler_001 import *
from problems._002.euler_002 import *
from problems._003.euler_003 import *
from problems._004.euler_004 import *
from problems._005.euler_005 import *
from problems._006.euler_006 import *
from problems._007.euler_007 import *
from problems._008.euler_008 import *
from problems._009.euler_009 import *
from problems._010.euler_010 import *
from problems._011.euler_011 import *


class EulerTests(unittest.TestCase):
    def test_euler__001(self):
        self.assertEqual(sum3or5_naive(10), 23)
        self.assertEqual(sum3or5_list_comprehension(10), 23)
        self.assertEqual(sum3or5_naive(1000), 233168)
        self.assertEqual(sum3or5_list_comprehension(1000), 233168)

    def test_euler__002(self):
        self.assertEqual(sum_fib(4000000), 4613732)

    def test_euler__003(self):
        self.assertEqual(largest_prime(), 6857)

    def test_euler__004(self):
        self.assertEqual(test_for_palindromes(100, 100), 9009)
        self.assertEqual(test_for_palindromes(1000, 1000), 906609)

    def test_euler__005(self):
        self.assertEqual(divisible_by_range(2520, 1, 10), True)
        self.assertEqual(euler_005(), 232792560)

    def test_euler__006(self):
        self.assertEqual(sum_of_squares(10), 385)
        self.assertEqual(square_of_sum(10), 3025)
        self.assertEqual(difference_of_squares(10), 2640)
        self.assertEqual(difference_of_squares(100), 25164150)

    def test_euler__007(self):
        self.assertEqual(sieve_of_eratosthenes(1000000, 6), 13)
        self.assertEqual(sieve_of_eratosthenes(1000000, 10001), 104743)

    def test_euler__008(self):
        self.assertEqual(find_highest_adjacent_product(4), 5832)
        self.assertEqual(find_highest_adjacent_product(13), 23514624000)

    def test_euler__009(self):
        self.assertEqual(is_pythagorean_triplet(3,4,5), True)
        self.assertEqual(findXYZ(500, 500, 500), 31875000)

    def test_euler__010(self):
        self.assertEqual(euler_010(10), 17)
        self.assertEqual(euler_010(2000000), 142913828922)

    def test_euler__011(self):
        self.assertEqual(euler_011(), 70600674)

if __name__ == '__main__':
    unittest.main()
