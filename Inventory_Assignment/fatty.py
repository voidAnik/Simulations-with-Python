
# inventory

import numpy as np
from matplotlib import pyplot as plt

np.random.seed(0)

initial_inventory = 3
ending_inventory = 0

shortage = 0
shortage_list = []

order_quantity = 8
order_interval_days = 2
demand_list = [0, 1, 2, 3, 4]
demand_prob = [0.10, 0.25, 0.35, 0.21, 0.09]
lead_time = [1, 2, 3]
lead_time_prob = [0.6, 0.3, 0.1]
k = []

maximum_capacity = int(input("Maximum Inventory : "))
review_period = int(input("Enter review period : "))  # n

ending_unit_list = []
total_ending_units = 0

for i in range(1, 10):
    print(" Cycle : ", i)

    for j in range(1, review_period + 1):
        print("Day : " + str(j))

        if order_interval_days > 0:
            order_interval_days = order_interval_days - 1

        elif order_interval_days != -1:  # stock refill
            order_interval_days = -1
            initial_inventory = order_quantity + initial_inventory
            order_quantity = 0

        print("Initial Inventory : ", initial_inventory)
        demand = np.random.choice(a=demand_list, p=demand_prob)

        total_demand = demand + shortage
        ending_inventory = initial_inventory - total_demand
        if ending_inventory < 0:
            shortage = -(ending_inventory)
            ending_inventory = 0

        elif ending_inventory >= 0:
            shortage = 0

        # after one cycle

        initial_inventory = ending_inventory

        shortage_list.append(shortage)
        ending_unit_list.append(ending_inventory)
        total_ending_units = total_ending_units + ending_inventory

        print("Demand : ", demand)
        print("Ending Inventory : ", ending_inventory)
        print("Shortage quantity : ", shortage)

        if j < 5:
            print("Days until order arrives : ", order_interval_days)
            print("Order Quantity :  ", order_quantity)

    order_quantity = maximum_capacity - ending_inventory
    order_interval_days = np.random.choice(a=lead_time, p=lead_time_prob)

    print("Days until order arrives : ", order_interval_days)
    print("Order Quantity :  ", order_quantity)

average_ending_units = total_ending_units / (review_period * 10)
shortage_list = np.array(shortage_list)
shortage_day = np.count_nonzero(shortage_list)
print("Average ending units : ", average_ending_units)
print("Number of days shortage occurs : ", shortage_day)

# Plot
print(len(ending_unit_list))
for i in range(1, review_period*9+1):
    k.append(str(i))
print(len(k))
plt.title("Inventory level and Days")
plt.xlabel("Number of days")
plt.ylabel("Ending Inventory of each day")
plt.plot(k, ending_unit_list)
plt.show()