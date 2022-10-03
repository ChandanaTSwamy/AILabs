import random as r
import math as m
import numpy as np


cities = {}
distance = {}

with open("inst-21.tsp") as filearr:
    paths = int(filearr.readline())

    for i in range(paths):
        linearr = filearr.readline()

        splittxt = linearr.split()
        cities[int(splittxt[0])] = (int(splittxt[1]), int(splittxt[2]))

print(cities)

distance = np.empty((0, 3), int)
shortest_path = np.empty((0, 3), int)

for i in range(1, (paths + 1)):
    # print("Value of i before j loop", i)
    d = 0
    for j in range(1, (paths + 1)):
        if i == j:
            pass
        else:
            d = round(m.sqrt(abs(((cities[i][0] - cities[j][0]) ^ 2) + ((cities[i][1] - cities[j][1]) ^ 2))))
            distance = np.append(distance, np.array([[i, j, d]]), axis=0)

# print(distance)
# ==================================================================================
length = len(distance)

sdarr = np.empty((0, 3), int)
starting_point = 1
next_startpoint = 1
sparr = np.array([next_startpoint])

for i in range(1, paths):
    sd = 1000000
    # print("Printing i value:", i)
    for j in range(length):
        # print("inside j: ", j)
        if distance[j, 0] != next_startpoint:
            # print("inside outer if ")
            pass
        else:
            # print("inside outer else ")
            # print("distance[j, 2] : ", distance[j, 2])
            if sd > distance[j, 2]:
                # print("inside inner if ")
                # print("Printing distance[j, 1] ", distance[j, 1])
                s = np.where(sparr == distance[j, 1])
                size = len(sparr[s])
                # print("size:", size)
                if size == 0:
                    # print("inside inner-inner if ")
                    sd = distance[j, 2]
                    sdarr = np.array([distance[j, 0], distance[j, 1], distance[j, 2]])
            else:
                # print("inside inner else ")
                pass

    next_startpoint = sdarr[1]

    sparr = np.concatenate((sparr, np.array([next_startpoint])))
    shortest_path = np.append(shortest_path, np.array([sdarr]), axis=0)

# shortest_path = np.append(shortest_path, np.array([sdarr]), axis=0)

result = np.where(distance == next_startpoint)
# print("next_startpoint", next_startpoint)
coOrdLen = len(result[0])

for i in range(coOrdLen):
    if distance[result[0][i], result[1][i]] != next_startpoint:
        pass
    elif distance[result[0][i], result[1][i]] == next_startpoint and result[1][i] != 0:
        pass
    else:
        if distance[result[0][i], 1] != starting_point:
            pass
        else:
            sdarr = np.array([distance[result[0][i], 0], distance[result[0][i], 1], distance[result[0][i], 2]])
            shortest_path = np.append(shortest_path, np.array([sdarr]), axis=0)

print("Printing nearest neighbour solution:\n", shortest_path)

# ==================================================================================

print("\n Start - Random Nearest Neighbour Solution")

"""
loop_variable = 10
for i in range(loop_variable):
    random_sp = r.choice(list(cities.keys()))
    print("For loop i:", i, ", random starting point is:", random_sp)
"""
