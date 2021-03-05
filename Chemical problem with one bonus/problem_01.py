import copy
array = [[0, 1, 0, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 1, 1, 0, 1],
         [0, 1, 0, 0, 1],
         [0, 0, 0, 0, 0]]


def printMatrix(time, array):
    print("TIME-", time, ":")
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in array]))
    print("\n")


printMatrix(0, array)
for t in range(1, 20):
    temp_array = copy.deepcopy(array)
    for i in range(5):
        for j in range(5):
            A_alive = 0
            D_alive = 0
            # print("for index", i, j)
            iList = [i - 1, i, i + 1]
            jList = [j - 1, j, j + 1]

            # for all side logic
            if i == 0:
                iList = [i, i + 1]
                jList = [j - 1, j, j + 1]
            if j == 0:
                iList = [i - 1, i, i + 1]
                jList = [j, j + 1]
            if i == 0 and j == 0:
                iList = [i, i + 1]
                jList = [j, j + 1]
            if i == 4:
                iList = [i - 1, i]
                jList = [j - 1, j, j + 1]
            if j == 4:
                iList = [i - 1, i, i + 1]
                jList = [j - 1, j]
            if i == 0 and j == 4:
                iList = [i, i + 1]
                jList = [j - 1, j]
            if i == 4 and j == 0:
                iList = [i, i - 1]
                jList = [j, j + 1]
            if i == 4 and j == 4:
                iList = [i - 1, i]
                jList = [j - 1, j]

            for t_i in iList:
                for t_j in jList:
                    if t_i != i or t_j != j:
                        if array[i][j] == 1:
                            if array[t_i][t_j] == 1:
                                A_alive += 1
                        else:
                            if array[t_i][t_j] == 1:
                                D_alive += 1
            # print("alive cell alive neighbours = ", A_alive)
            # print("Dead cell alive neighbours =", D_alive)
            if array[i][j] == 1:
                if 2 < A_alive or A_alive < 2:
                    # print("alive = die")
                    temp_array[i][j] = 0
                if A_alive == 2:
                    # print("alive = alive")
                    temp_array[i][j] = 1
            else:
                if D_alive == 2 or D_alive == 3:
                    # print("dead = alive")
                    temp_array[i][j] = 1

    array = copy.deepcopy(temp_array)
    printMatrix(t, array)
