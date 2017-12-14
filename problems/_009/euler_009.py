# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def is_pythagorean_triplet(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

def findXYZ(a, b, c):
    for x in range(1, a):
        for y in range(1, b):
            for z in range(1, c):
                if (x + y + z) == 1000 and is_pythagorean_triplet(x, y, z):
                    return x * y * z

