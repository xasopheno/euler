import itertools

# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

permutations = itertools.permutations(items)


def nth(iterable, n, default=None):
    return next(itertools.islice(iterable, n, None), default)


def euler_024():
    millionth = nth(permutations, 999999)
    list_millionth = list(millionth)
    joined = ''.join([str(x) for x in list_millionth])
    return int(joined)
