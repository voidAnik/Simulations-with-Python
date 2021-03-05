import random
import math

random.seed(0)

x_values = [500, 1000, 5000, 10000]
a1, b1 = 0, 2
a2, b2 = 2, 4

for i in x_values:

    # For 1st curve
    f_sum1,f_sum2 = 0, 0
    f_square_sum1,f_square_sum2 = 0, 0

    for j in range(i):
        x1 = random.uniform(b1,a1)
        x2 = random.uniform(b2,a2)
        func_value1 = 2 * x1
        func_value2 = 8 - 2 * x2

        f_sum1 = f_sum1 + func_value1
        f_square_sum1 = f_square_sum1 + math.pow(func_value1, 2)
        f_sum2 = f_sum2 + func_value2
        f_square_sum2 = f_square_sum2 + math.pow(func_value2, 2)

    f_avg1 = f_sum1 / i
    f_square_avg1 = f_square_sum1 / i
    integral_value1 = (b1 - a1) * f_avg1
    error1 = ((b1 - a1) / math.sqrt(int(i))) * math.sqrt(f_square_avg1 - (math.pow(f_avg1, 2)))
    f_avg2 = f_sum2 / i
    f_square_avg2 = f_square_sum2 / i
    integral_value2 = (b1 - a1) * f_avg2
    error2 = ((b1 - a1) / math.sqrt(int(i))) * math.sqrt(f_square_avg2 - (math.pow(f_avg2, 2)))

    # Final result
    integral_value = integral_value1 + integral_value2
    error = error1 * error2

    print("For trials = ", i)
    print("Integral value = ", integral_value)
    print("Error = ", error, "\n")
