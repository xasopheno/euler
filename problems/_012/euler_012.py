import math

def triangular_number(i):
    value = sum(range(i + 1))
    print(value)
    return value

triangular_numbers = [triangular_number(i) for i in range(9)]
maximum = 0

for number in triangular_numbers:
    i = 500000
    counter = 0
    for i in range(1, int(math.sqrt(number) + 1)):
        print(number, i)
        if number % i == 0:
            counter += 1
            if counter > maximum:
                maximum += 1
                print(maximum, '-', number)
            # break
        if counter == 500:
            print(number)
            break
    if counter == 500:
        print(number)
        break
