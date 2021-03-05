import math
import random
import matplotlib.pyplot as plt

random.seed(0)

# buffon's needle
d = 4
l = 2
hits = 0
n = 1000
hit_x = []
hit_y = []
miss_x = []
miss_y = []
for i in range(0, n):
    D = random.uniform(0, d / 2)
    theta = random.uniform(0, 3.1416)
    if D <= (l / 2) * math.sin(theta):
        hits = hits + 1
        hit_x.append(theta)
        hit_y.append(D)
    else:
        miss_x.append(theta)
        miss_y.append(D)
pi = (2 * l / d) * (n / hits)
print(pi)
plt.scatter(hit_x, hit_y, color="red", label="Hit points")
plt.scatter(miss_x, miss_y, color="green", label="Miss points")
plt.ylabel('D')
plt.xlabel('Value of theta')
plt.title('Buffons needle')
plt.legend()
plt.show()
