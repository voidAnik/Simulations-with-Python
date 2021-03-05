import numpy as np
from matplotlib import pyplot as plt

np.random.seed(0)

# m = 11  # Maximum capacity
# n = 5  # review period
beginning_inventory = 3
ending_inventory = 0
total_ending_inventory = 0
daily_demand = 0
shortage_quantity = 0
shortage_count = 0
order_quantity = 8
days_until_order_arrives = 2
#####
demandList = [0, 1, 2, 3, 4]
demandProbability = [0.10, 0.25, 0.35, 0.21, 0.09]
leadTime = [1, 2, 3]
leadTime_prob = [0.6, 0.3, 0.1]
ending_inventory_list = []
x = []

m = int(input("Maximum inventory: "))
n = int(input("Number of Days: "))

for cycle in range(1, 6):
    print("Cycle No: ", cycle)
    for day in range(1, n + 1):
        print("Review Period: ", day)
        # checking waiting to arrives finishes
        if days_until_order_arrives == 0:
            beginning_inventory += order_quantity
            order_quantity = 0

        else:  # waiting for the day to arrive
            days_until_order_arrives -= 1

        # creating random variable for daily demand
        daily_demand = np.random.choice(a=demandList, p=demandProbability)

        print("Daily Demand: ", daily_demand)
        print("Beginning Inventory: ", beginning_inventory)

        total_demand = daily_demand + shortage_quantity  # to count shortages within
        if total_demand < beginning_inventory:
            ending_inventory = beginning_inventory - total_demand
            shortage_quantity = 0
        else:
            shortage_quantity = total_demand - beginning_inventory
            ending_inventory = 0
            shortage_count += 1
        print("Shortage Quantity: ", shortage_quantity)
        print("Ending Inventory: ", ending_inventory)

        beginning_inventory = ending_inventory  # setting ending in beginning at last
        ending_inventory_list.append(ending_inventory)
        total_ending_inventory += ending_inventory

        if day == n:  # checking to refill on the last day of a cycle
            order_quantity = m - ending_inventory
            days_until_order_arrives = np.random.choice(a=leadTime, p=leadTime_prob)

        print("Days until Order Arrives : ", days_until_order_arrives)
        print("Order Quantity :  ", order_quantity)
        print(" ")

average_ending_inventory = total_ending_inventory / (5 * n)
print("Average Ending Units: ", average_ending_inventory)
print("Shortage occurs on " + str(shortage_count) + " days")

for i in range(1, 5 * n + 1):
    x.append(str(i))
# Plot
plt.title("Ending inventory level and Days")
plt.xlabel("Number of days")
plt.ylabel("Ending Inventory of each day")
plt.plot(x, ending_inventory_list)
plt.show()
