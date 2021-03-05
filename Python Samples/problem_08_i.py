import matplotlib.pyplot as plt

#toothpaste
x = [1, 2, 3, 4, 5, 6]
y1 = [2500, 2630, 2140, 3400, 3600, 2760]
# plotting the toothpaste points
plt.plot(x, y1, label="Toothpaste")

# facewash points
y2 = [1500, 1200, 1340, 1130, 1740, 1555]
# plotting the facewash points
plt.plot(x, y2, label="Facewash")

# shampoo points
y3 = [5200, 5100, 4550, 5870, 4560, 4890]
# plotting the shampoo points
plt.plot(x, y3, label="Shampoo")

# Moisturizer points
y4 = [9200, 6100, 9550, 8870, 7760, 7490]
# plotting the Moisturizer points
plt.plot(x, y4, label="Moisturizer")

# soap point
y5 = [1200, 2100, 3550, 1870, 1560, 1890]
# plotting the soap points
plt.plot(x, y5, label="Soap")

# naming the x axis
plt.xlabel('month no.')
# naming the y axis
plt.ylabel('sales unit')
# giving a title to my graph
plt.title('sales data graph!')

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()