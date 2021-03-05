import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
# Moisturizer points
y = [9200, 6100, 9550, 8870, 7760, 7490]
# plotting the Moisturizer points
plt.scatter(x, y, color="green", label="Moisturizer sales")


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