import random
import math
random.seed(0)

x_values = [500, 1000, 5000, 10000]
a = 0
b = 2
errors = []

for i in x_values:

    f_sum = 0
    f_square_sum = 0

    for j in range(i):
        x = random.uniform(a, b)
        func_value = math.sqrt(4-math.pow(x, 2))

        f_sum = f_sum + func_value
        f_square_sum = f_square_sum + math.pow(func_value, 2)

    f_avg = f_sum / i
    f_square_avg = f_square_sum / i

    integral_value = (b - a) * f_avg
    area = 4 * integral_value
    error = ((b - a) / math.sqrt(int(i))) * math.sqrt(f_square_avg - (math.pow(f_avg, 2)))
    errors.append(error)

    print("For trials = ", i)
    print("Integral value = ", integral_value)
    print("Area = ", area)
    print("Error = ", error, "\n")
