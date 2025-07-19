n = int(input("Введите высоту цифрового треугольника: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
        if j == i:
            while j > 1:
                print(j-1, end="")
                j -= 1
    print()