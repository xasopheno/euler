
def sum_diagnols(n):
    total_list = [1]
    total = 1
    counter = 2
    while total < n * n:
        for i in range(4):
            total += counter
            total_list.append(total)
        counter += 2

    return sum(total_list)

