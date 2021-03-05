listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
listThree1,listThree2,listThree = [],[],[]

for i in range(1,len(listOne),2):
    listThree1.append(listOne[i])
print("Element at odd-index positions from list one:",listThree1)

for i in range(0,len(listTwo),2):
    listThree2.append(listTwo[i])
print("Element at odd-index positions from list one:",listThree2)

listThree = listThree1+listThree2
print("Printing Final third list :",listThree)

