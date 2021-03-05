import random
import matplotlib.pyplot as plt
import math

random.seed(0)
trials = [100, 1000, 5000, 10000]
hits = 0
center_circle = [2, 2]
r = 1.5
r_x, r_y = 4, 4

pi_values, area_circles, errors = [], [], []
for n in trials:
    hit_x, hit_y, miss_x, miss_y = [], [], [], []
    hits = 0

    for i in range(n):
        x = random.uniform(0, r_x)
        y = random.uniform(0, r_y)
        if math.sqrt((x - center_circle[1]) ** 2 + (y - center_circle[1]) ** 2) <= r:
            hits = hits + 1
            hit_x.append(x)
            hit_y.append(y)
        else:
            miss_x.append(x)
            miss_y.append(y)

    pi = ((r_x * r_y) / math.pow(r, 2)) * (hits / n)
    error = abs(float(pi) - 3.1416)
    area_circle = (r_x * r_y) * (hits / n)
    pi_values.append(pi)
    errors.append(error)
    area_circles.append(area_circle)
    print("For trials of = " + str(n) + ", Value of pi is %.3f " % pi + ", Area of circle is = " + str(area_circle))

    plt.scatter(hit_x, hit_y, color="red", label="Hits")
    plt.scatter(miss_x, miss_y, color="green", label="Missed")

    plt.ylabel('Y-label')
    plt.xlabel('X-label')
    plt.title("For trials of n = " + str(n))
    plt.legend()
    plt.show()

x = ['100', '1000', '5000', '10000']
# for pi values
plt.bar(x, pi_values)  # pi_value
plt.xlabel('number of trials')
# frequency label
plt.ylabel('value of PI')
# plot title
plt.ylim(0, 5)
plt.title('PI values')
plt.show()

# for Error value
plt.bar(x, errors, color='red')
plt.xlabel('number of trials')
# frequency label
plt.ylabel('value of PI')
# plot title
plt.ylim(0, 1)
plt.title('ERROR values')
plt.show()

# for area of the circle
plt.bar(x, area_circles, color='yellow')
plt.xlabel('number of trials')
# frequency label
plt.ylabel('area of the circle')
# plot title
plt.ylim(0, 8)
plt.title('Area of the Circle')
plt.show()
