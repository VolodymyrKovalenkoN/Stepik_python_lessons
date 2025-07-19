# 10, 5, 0.5, = 100
#  10 20 200
for i in range(1, 11):
    for j in range(1, 21):
        for k in range(1, 201):
            if 10 * i + 5 * j + 0.5 * k == 100 and i + j + k == 100:
                print("i =", i, "j =", j, "k =", k)