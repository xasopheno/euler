def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def sumDigets():
    strNum = str(factorial(100))
    total = sum([int(i) for i in strNum])
    print(total)

sumDigets()
