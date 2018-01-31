def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


print(fib(10))

# def dynamicFibo(n,table = []):
#     while len(table) < n+1: table.append(0) #this does the same thing except it doesn't change the reference to `table`
#     #base case
#     if n <= 1:
#         return n
#     #recursive case
#     else:
#         if table[n-1] == 0:
#             table[n-1] = dynamicFibo(n-1)
#
#         if table[n-2] == 0:
#             table[n-2] = dynamicFibo(n-2)
#
#         table[n] = table[n-2] + table[n-1]
#     return table[n]

def dynamicFibo(n, table=[]):
    while len(table) < n+1: table.append(0)
    if n <= 1:
        return n
    else:
        if table[n-1] == 0:
            table[n-1] = dynamicFibo(n-1)

        if table[n-2] == 0:
            table[n-2] = dynamicFibo(n-2)

        table[n] = table[n-2] + table[n-1]

    return table[n]

print(dynamicFibo(900))
