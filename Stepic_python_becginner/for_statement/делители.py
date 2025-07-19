from math import ceil


n = int(input("Enter number: "))
for i in range(1, n + 1):
    count = 0
    for j in range(1, ceil(i) + 1):
        if i % j == 0:
            count += 1
    print(i, "+" * count, sep="")