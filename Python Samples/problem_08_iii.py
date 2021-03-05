import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y1 = [2500, 2630, 2140, 3400, 3600, 2760]
# facewash points
y2 = [1500, 1200, 1340, 1130, 1740, 1555]
# shampoo points
y3 = [5200, 5100, 4550, 5870, 4560, 4890]
# Moisturizer points
y4 = [9200, 6100, 9550, 8870, 7760, 7490]
# soap point
y5 = [1200, 2100, 3550, 1870, 1560, 1890]
y=[]
for i in range(len(y1)):
    temp=y1[i]+y2[i]+y3[i]+y4[i]+y5[i]
    y.append(temp)

# naming the x axis
plt.xlabel('month no.')
# naming the y axis
plt.ylabel('sales unit')
# giving a title to my graph
plt.title('number of sells each month bar graph!')
plt.bar(x,y)
plt.show()
