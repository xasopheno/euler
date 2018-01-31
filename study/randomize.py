# Write an algorithm to randomize the order of elements in an array (iteratively, then recursively, then in O(n) time).
import random

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def randomize_list(li):
    l = li.copy()
    print(l)
    for index in range(len(l)):
        rand = random.randint(0, len(l) - 1)
        l[index], l[rand] = l[rand], l[index]
    print(l)
    print('__________')
    return l

print(myList != randomize_list(myList))
print(randomize_list(myList) != randomize_list(myList))

print('__________')
print(myList)
random.shuffle(myList)
print(myList)
