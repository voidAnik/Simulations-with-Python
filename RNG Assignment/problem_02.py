# Tousworthe method
# Omar Faruk - 011163092

import matplotlib.pyplot as plt

r = 3
q = 5
l = 4
random_count = 1000
b = [1, 1, 1, 1]
x = []
u = []

for i in range(4, (random_count * l)):  # to make 1000 random numbers need 1000 * l bits
    b_new = b[i - r] ^ b[i - q]
    b.append(b_new)

for i in range(0, len(b), l):
    b_seg = b[i: i + l]
    seg_str = ""
    for j in b_seg:
        seg_str = seg_str + str(j)
    w = int(seg_str, 2)
    u.append(w / (2 ** l))
    x.append(int(i / 4))

print(u)
print(x)
plt.bar(x, u)
plt.xlabel('index of a random number, i')
plt.ylabel('the random number, u')
plt.title('random number generate with tousworthe')
plt.show()
