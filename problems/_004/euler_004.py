def palindromic_number(num):
    num_string = str(num)
    len_string = len(num_string)
    for i in range(0, len_string):
        if num_string[i] != num_string[-i-1]:
            return False
        if i == len_string -1:
            return True


def test_for_palindromes(a, b):
    max_num = 0
    for x in range(a):
        for y in range(b):
            product = x * y
            if palindromic_number(product) and product > max_num:
                max_num = product

    return max_num
