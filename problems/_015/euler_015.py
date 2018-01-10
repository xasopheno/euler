def route_num(cube_size):
    intersection = [1] * cube_size
    for i in range(cube_size):
        for j in range(i):
            intersection[j] = intersection[j]+intersection[j-1]
            print(intersection[j])
        intersection[i] = 2 * intersection[i - 1]
    print(intersection)
    return intersection[cube_size - 1]

answer = route_num(4)
print(answer)
