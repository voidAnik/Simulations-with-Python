import random
import math
random.seed(0)

x_values = [500, 1000, 5000, 10000]
a = 0
b = 4

for i in x_values:

    f_sum = 0
    f_square_sum = 0

    for j in range(i):
        x = random.uniform(a, b)
        if 0 <= x <= 2:
            func_value = 2 * x
        else:
            func_value = 8 - 2 * x

        f_sum = f_sum + func_value
        f_square_sum = f_square_sum + math.pow(func_value, 2)

    f_avg = f_sum / i
    f_square_avg = f_square_sum / i

    integral_value = (b - a) * f_avg
    error = ((b - a) / math.sqrt(int(i))) * math.sqrt(f_square_avg - (math.pow(f_avg, 2)))

    print("For trials = ", i)
    print("Integral value = ", integral_value)
    print("Error = ", error, "\n")
