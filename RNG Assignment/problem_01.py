# Wichman / Hill method
# Omar Faruk - 011163092

import matplotlib.pyplot as plt

trial = [100, 1000, 5000]
for t in trial:
    print(t, "random numbers =")
    z1 = [12, 7]
    z2 = [3, 5]
    z3 = [2, 7]
    u1, u2, u3 = [], [], []
    u = []
    x = []

    for i in range(2, t):
        z1_new = (13 * z1[i - 1] + 11 * z1[i - 2] + 3) % 16
        z1.append(z1_new)

        z2_new = (12 * z2[i - 1] ** 2 + 13 * z2[i - 2]) % 17
        z2.append(z2_new)

        z3_new = (z3[i - 1] ** 3 + z3[i - 2] ** 2) % 15
        z3.append(z3_new)

    for i in range(0, t):
        u1.append(z1[i] / 16)
        u2.append(z2[i] / 17)
        u3.append(z3[i] / 15)
        temp = int(u1[i] + u2[i] + u3[i])
        u_new = (u1[i] + u2[i] + u3[i]) - temp
        u.append(u_new)
        x.append(i)

    print(u)
    plt.bar(x, u)
    plt.xlabel('index of a random number')
    plt.ylabel('the random number')
    plt.title('random number generate with Wichman / Hill')
    plt.show()
