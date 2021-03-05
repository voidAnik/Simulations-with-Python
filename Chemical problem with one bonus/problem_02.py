# A + B = C
import math
a = [50]
b = [50]
c = [30]
kf = 0.05
kb = 0.01
delta_t = 0.2
threshold = 0.01
for t in range(0, 5):
    print("at time= ,", t)
    a_rate = 2 * kb * c[t] - kf * math.pow(a[t], 2) * b[t]
    b_rate = 2 * kb * c[t] - kf * math.pow(a[t], 2) * b[t]
    c_rate = kf * (a[t] ** 3) * b[t] - kb * c[t]

    # a_rate = round((2 * kb * c[t] - kf * ((a[t]) ** 2) * b[t]), 3)
    # b_rate = round((2 * kb * c[t] - kf * ((a[t]) ** 2) * b[t]), 3)
    # c_rate = round((kf * ((a[t]) ** 3) * b[t] - kb * c[t]), 3)
    print("rate a,b,c =", a_rate, b_rate, c_rate)

    # a.append(round((a[t] + a_rate * delta_t), 3))
    # b.append(round((b[t] + b_rate * delta_t), 3))
    # c.append(round((c[t] + c_rate * delta_t), 3))

    a.append(a[t] + a_rate * delta_t)
    b.append(b[t] + b_rate * delta_t)
    c.append(c[t] + c_rate * delta_t)
    print("a,b,c =", a[t], b[t], c[t])

    diff_a = abs(a[t + 1] - a[t])
    diff_b = abs(b[t + 1] - b[t])
    diff_c = abs(c[t + 1] - c[t])
    print("diff of a,b,c =", diff_a, diff_b, diff_c)
    if diff_a < threshold and diff_b < threshold and diff_c < threshold:
        print("It's an equilibrium point.")
        break

