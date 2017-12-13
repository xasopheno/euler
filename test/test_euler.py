import unittest

from problems._001.euler_001 import *
from problems._002.euler_002 import *


class EulerTests(unittest.TestCase):
    def test_euler__1(self):
        self.assertEqual(sum3or5_naive(10), 23)
        self.assertEqual(sum3or5_list_comprehension(10), 23)
        self.assertEqual(sum3or5_naive(1000), 233168)
        self.assertEqual(sum3or5_list_comprehension(1000), 233168)

    def test_euler__2(self):
        self.assertEqual(sum_fib(4000000), 4613732)


if __name__ == '__main__':
    unittest.main()
