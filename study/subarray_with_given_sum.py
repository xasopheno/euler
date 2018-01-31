test1 = [5, 12]
test1_array = [1, 2, 3, 7, 5]
test2 = [10, 15]
test2_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def sub_array_with_given_sum(info, array):
    total = array[0]
    size = info[0]
    goal = info[1]
    for i in range(1, size):
        for j in range(i, size):
            if total == goal:
                print(i, j)
                return [i, j]
            elif total > goal:
                total = array[i]
            else:
                total += array[j]
    return []

print(sub_array_with_given_sum(test1, test1_array) == [2, 4])
print(sub_array_with_given_sum(test2, test2_array) == [1, 5])
