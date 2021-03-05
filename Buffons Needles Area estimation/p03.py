import random
import matplotlib.pyplot as plt
import math

random.seed(0)
trials = [100, 1000, 5000, 10000]
hits = 0
r_x, r_y = 8, 4
r_x1, r_x2 = [0, 4], [4, 8]
for n in trials:
    hit_x, hit_y, miss_x, miss_y = [], [], [], []
    hits = 0

    for i in range(n):
        x = random.uniform(0, r_x)
        y = random.uniform(0, r_y)
        if r_x1[0] <= x <= r_x1[1]:
            y_curve = math.sqrt(4 * x)
        else:
            y_curve = 8-x
        if y <= y_curve:
            hits = hits + 1
            hit_x.append(x)
            hit_y.append(y)
        else:
            miss_x.append(x)
            miss_y.append(y)

    curve_area = (r_x * r_y) * (hits / n)
    print("For trials of = " + str(n) + ", Area of the curve is = %.3f" % curve_area)

    plt.scatter(hit_x, hit_y, color="red", label="Hits")
    plt.scatter(miss_x, miss_y, color="green", label="Missed")

    plt.ylabel('Y-label')
    plt.xlabel('X-label')
    plt.title("For trials of n = " + str(n))
    plt.legend()
    plt.show()
