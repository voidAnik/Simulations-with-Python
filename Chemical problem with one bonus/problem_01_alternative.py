import copy

array = [[0, 1, 0, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 1, 1, 0, 1],
         [0, 1, 0, 0, 1],
         [0, 0, 0, 0, 0]]

temp_array = []


def printMatrix(time, array):
    print("TIME-", time, ":")
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in array]))
    print("\n")


def checkN(rS, rE, cS, cE, c1, c2):
    # if rS<0:
    #     rS = 0
    # if rE>4:
    #     rS = 4
    # if cS<0:
    #     cS = 0
    # if cE>4:
    #     cE = 4
    alive = 0
    for i in range(rS,rE):
        print("i =",i)
        for j in range(cS,cE):
            print("j=",j)
            if i != c1 or j != c2:
                if array[i][j] == 1:
                    alive += 1
                    print("ALIVE")
    return alive


printMatrix(0, array)
for t in range(1, 20):
    temp_array = copy.deepcopy(array)
    for i in range(5):
        for j in range(5):
            # A_alive = 0
            # D_alive = 0
            print("for index", i, j)
            # iList = [i - 1, i, i + 1]
            # jList = [j - 1, j, j + 1]

            # for all side logic

            if i == 0 and j == 0:
                A_alive = checkN(i, i + 1, j, j + 1, i, j)
            elif i == 4 and j == 4:
                A_alive = checkN(i - 1, i, j - 1, j, i, j)
            elif i == 0:
                # iList = [i, i + 1]
                # jList = [j - 1, j, j + 1]
                A_alive = checkN(i, i + 1, j - 1, j + 1, i, j)
            elif j == 0:
                A_alive = checkN(i - 1, i + 1, j, j + 1, i, j)
            elif i == 4:
                A_alive = checkN(i - 1, i, j - 1, j + 1, i, j)
            elif j == 4:
                A_alive = checkN(i - 1, i + 1, j - 1, j, i, j)
            elif i == 0 and j == 4:
                A_alive = checkN(i, i + 1, j - 1, j, i, j)
            elif i == 4 and j == 0:
                A_alive = checkN(i - 1, i, j, j + 1, i, j)

            # A_alive = checkN(i-1, i+1, j-1, j+1, i, j, array)

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
                if A_alive == 2 or A_alive == 3:
                    # print("dead = alive")
                    temp_array[i][j] = 1

    array = copy.deepcopy(temp_array)
    printMatrix(t, array)
