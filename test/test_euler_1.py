import unittest
from problems.euler_1 import *

class EulerTests(unittest.TestCase):
    def test_euler__1(self):
        self.assertEqual(sum3or5_naive(10), 23)
        self.assertEqual(sum3or5_list_comprehension(10), 23)
        self.assertEqual(sum3or5_naive(1000), 233168)
        self.assertEqual(sum3or5_list_comprehension(1000), 233168)

    def test_euler__2(self):
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
