def rem_duplicate(l):
    f_list = []
    for n in l:
        if n not in f_list:
            f_list.append(n)
    return f_list

int_list=list(input("Enter some integer= "))
print(rem_duplicate(int_list))