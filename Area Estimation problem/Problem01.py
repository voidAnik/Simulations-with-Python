import matplotlib.pyplot as plt
import random
import math

random.seed(0)

x_values = [500, 1000, 5000, 10000]
a = 0
b = 5
errors = []

for i in x_values:

    f_sum = 0
    f_square_sum = 0

    for j in range(i):
        x = random.uniform(a, b)
        func_value = (math.pow(x, 2) * (math.exp(-x)))
        f_sum = f_sum + func_value
        f_square_sum = f_square_sum + math.pow(func_value, 2)

    f_avg = f_sum / i
    f_square_avg = f_square_sum / i
    integral_value = (b - a) * f_avg
    error = ((b - a) / math.sqrt(i)) * math.sqrt(f_square_avg - (f_avg ** 2))
    errors.append(error)

    print("For trial = ", i)
    print("Integral value = ", integral_value)
    print("Error = ", error, "\n")

x = ['500', '1000', '5000', '10000']
plt.bar(x, errors)
plt.xlabel('trials')
plt.ylabel('error')
plt.title('Bar chart for Errors')
plt.show()
