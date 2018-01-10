numStr = str(2 ** 1000)
total = 0
for i in range(len(numStr)):
    total += int(numStr[i])

print(total)
