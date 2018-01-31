def answer(total_lambs):
    """
    Lovely Lucky LAMBs
    Args:
        total_lambs: the number of lambs available to distribute
    Returns:
        Int: the difference between the most `generous` and `stingiest` distributions of lambs given total_lambs
    """
    powers = _powers_of_2(total_lambs)
    fib = _fibonacci(total_lambs)
    return abs(powers - fib)


def _powers_of_2(total_lambs):
    """
    The most junior henchman (with the least seniority) gets exactly 1 LAMB
    A henchman will revolt if the person who ranks immediately above them gets
        more than double the number of LAMBs they do.
    If there are enough LAMBs left over such that another henchman could be added as the
        most senior while obeying the other rules, you must always add and pay that henchman.

    Args:
        total_lambs: the number of lambs available to distribute
    Returns:
        Int: Maximum num henchmen that can be paid without ever being paid more than double a subordinate
    """
    if total_lambs <= 1:
        return 1
    lambs_distributed = 0
    counter = 0
    rank = 1
    while lambs_distributed < total_lambs:
        lambs_distributed += rank
        if lambs_distributed > total_lambs:
            if _leftover_lambs(total_lambs, lambs_distributed, rank):
                counter += 1
        rank *= 2
        if lambs_distributed <= total_lambs:
            counter += 1
    return counter


def _leftover_lambs(total_lambs, lambs_distributed, rank):
    return total_lambs - (lambs_distributed - rank) >= rank/2 + rank/4


def _fibonacci(total_lambs):
    """
     A henchman will revolt if the amount of LAMBs given to their next two subordinates combined
        is more than the number of LAMBs they get

    Args:
        total_lambs: the number of lambs available to distribute
    Returns
        Int: count of fibonacci numbers below total_lambs
    """
    if total_lambs <= 1:
        return 1
    lambs_distributed = 0
    counter = 0
    a, b = 0, 1
    while lambs_distributed < total_lambs:
        lambs_distributed += b
        a, b = b, a + b
        if lambs_distributed <= total_lambs:
            counter += 1

    return counter


# Tests
print(answer(-1) == 0)
print(answer(0) == 0)
print(answer(1) == 0)
print(answer(10) == 1)
print(answer(13) == 1)
print(answer(143) == 3)
