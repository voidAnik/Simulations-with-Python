import math
import matplotlib.pyplot as plt

# D is chased by C, C is chased by B, B is chased by A. D is moving independently parallel to the y-axis.
x_D = [0]
y_D = [0]
x_C = [10]
y_C = [10]
x_B = [0]
y_B = [10]
x_A = [10]
y_A = [0]
v_A = 3
v_B = 5
v_C = 7
v_D = 2
distDC = []
distCB = []
distBA = []
shot_A, shot_B, shot_C, shot_D = 0, 0, 0, 0

for t in range(0, 21):
    distDC.append(math.sqrt((x_D[t] - x_C[t]) ** 2 + (y_D[t] - y_C[t]) ** 2))  # D is chased by C/ e.g: being chased
    # - chaser
    distCB.append(math.sqrt((x_C[t] - x_B[t]) ** 2 + (y_C[t] - y_B[t]) ** 2))  # C is chased by B
    distBA.append(math.sqrt((x_B[t] - x_A[t]) ** 2 + (y_B[t] - y_A[t]) ** 2))  # B is chased by A

    print("At time= ", t)
    print("x_A =", x_A[t], "y_A= ", y_A[t])
    print("x_B = ", x_B[t], "y_B=", y_B[t])
    print("x_C = ", x_C[t], "y_C=", y_C[t])
    print("x_D = ", x_D[t], "y_D=", y_D[t])
    print("\n")

    print("D to C distance =", distDC[t])
    print("C to B distance =", distCB[t])
    print("B to A distance =", distBA[t])
    print("\n")

    if distDC[t] < 5:
        print("Car C shoots Car D at time =", t)
        shot_D += 1
    if distCB[t] < 5:
        print("Car B shoots Car C at time =", t)
        shot_C += 1
    if distBA[t] < 5:
        print("Car A shoots Car B at time =", t)
        shot_B += 1
    print("\n")

    # to calculate and show only upto time=20
    # break if finished printing upto 20
    if t == 20:
        break

    # Appending new D
    x_D.append(0)
    y_D.append(y_D[t] + v_D)

    # Calculate new C
    sin = (y_D[t] - y_C[t]) / distDC[t]
    cos = (x_D[t] - x_C[t]) / distDC[t]
    x_C.append(x_C[t] + v_C * cos)
    y_C.append(y_C[t] + v_C * sin)

    # Calculate new B
    sin = (y_C[t] - y_B[t]) / distCB[t]
    cos = (x_C[t] - x_B[t]) / distCB[t]
    x_B.append(x_B[t] + v_B * cos)
    y_B.append(y_B[t] + v_B * sin)

    # Calculate new A
    sin = (y_B[t] - y_A[t]) / distBA[t]
    cos = (x_B[t] - x_A[t]) / distBA[t]
    x_A.append(x_A[t] + v_A * cos)
    y_A.append(y_A[t] + v_A * sin)

# the number of times each car got shot during the simulation.
print("Car A got shot ", shot_A, " times")
print("Car B got shot ", shot_B, " times")
print("Car C got shot ", shot_C, " times")
print("Car D got shot ", shot_D, " times")

# Plotting graph
plt.plot(x_D, y_D, label="Path D")
plt.plot(x_C, y_C, label="Path C")
plt.plot(x_B, y_B, label="Path B")
plt.plot(x_A, y_A, label="Path A")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()
