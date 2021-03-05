
int_list = list(input("Enter some integers= "))
even = 0
odd = 0
new_list = int_list.copy()
for num in int_list:
    if int(num) % 2 == 0:
        even += 1
        new_list.remove(num)
    else:
        odd += 1
        #new_list.append(num)

print("odd count is =",odd,"even count is =",even)

print("The list without even number",new_list)