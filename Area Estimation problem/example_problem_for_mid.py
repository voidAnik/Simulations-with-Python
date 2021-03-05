import random
import math

random.seed(0)

x_values = [500, 1000, 5000, 10000]
a1, b1 = 0, 2
a2, b2 = 2, 4

for i in x_values:

    # For 1st curve
    f_sum = 0
    f_square_sum = 0

    for j in range(i):
        x = random.uniform(a1, b1)
        func_value = 2 * x

        f_sum = f_sum + func_value
        f_square_sum = f_square_sum + math.pow(func_value, 2)

    f_avg = f_sum / i
    f_square_avg = f_square_sum / i
    integral_value1 = (b1 - a1) * f_avg
    error1 = ((b1 - a1) / math.sqrt(int(i))) * math.sqrt(f_square_avg - (math.pow(f_avg, 2)))

    # For 2nd curve
    f_sum = 0
    f_square_sum = 0
    for j in range(i):
        x = random.uniform(a2, b2)
        func_value = 8 - 2 * x

        f_sum = f_sum + func_value
        f_square_sum = f_square_sum + math.pow(func_value, 2)
    f_avg = f_sum / i
    f_square_avg = f_square_sum / i
    integral_value2 = (b2 - a2) * f_avg
    error2 = ((b2 - a2) / math.sqrt(int(i))) * math.sqrt(f_square_avg - (math.pow(f_avg, 2)))

    # Final result
    integral_value = integral_value1 + integral_value2
    error = error1 * error2

    print("For trials = ", i)
    print("Integral value = ", integral_value)
    print("Error = ", error, "\n")
