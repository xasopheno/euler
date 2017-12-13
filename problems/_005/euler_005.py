# 2520 is the smallest number that can be
# divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly
# divisible by all of the numbers from 1 to 20?

def divisible_by_range(num, a, b):
    for i in range(a, b + 1):
        if num % i != 0:
            return False
        if i == b:
            return True


def euler_005():
    a = 2520
    while True:
        if divisible_by_range(a, 1, 20):
            return a
        a += 2520

