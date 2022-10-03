# Travelling Salesman Problem

# from itertools import islice

import random as r
import math as m
import numpy as np
import time as t

cities = {}


def readInputFile(input_file):
    # cities = {}

    with open(input_file) as filearr:
        paths = int(filearr.readline())
        # print('No.of paths: ', paths)

        for i in range(paths):
            linearr = filearr.readline()
            # print(linearr.split())
            splittxt = linearr.split()
            # print(splittxt)
            cities[int(splittxt[0])] = (int(splittxt[1]), int(splittxt[2]))

    # print(cities)
    return paths


def distanceBetweenCities(paths):
    distance = {}
    distance = np.empty((0, 3), int)

    for i in range(1, (paths + 1)):
        # print("Value of i before j loop", i)
        d = 0
        for j in range(1, (paths + 1)):
            if i == j:
                pass
            else:
                """
                print ("Value of i", i)
                print("Value of j", j)
                """
                d = round(m.sqrt(abs(((cities[i][0] - cities[j][0]) ^ 2) + ((cities[i][1] - cities[j][1]) ^ 2))))
                distance = np.append(distance, np.array([[int(i), int(j), d]]), axis=0)

    # print(distance)
    return distance


def TSPSolutionNearestNeighbour(distance, paths, starting_point):
    length = len(distance)
    local_starting_point = starting_point
    next_startpoint = starting_point
    shortest_path = np.empty((0, 3), int)
    sdarr = np.empty((0, 3), int)
    sparr = np.array([next_startpoint])

    # print("paths value: ", paths)

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
                    # else:
                    # pass
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
            if distance[result[0][i], 1] != local_starting_point:
                pass
            else:
                sdarr = np.array([distance[result[0][i], 0], distance[result[0][i], 1], distance[result[0][i], 2]])
                shortest_path = np.append(shortest_path, np.array([sdarr]), axis=0)

    # print("Printing final solution inside sub-function:\n", shortest_path)
    return shortest_path


def TSPSolutionRandom (distance, paths, runs, output_filename):
    # print("Start - Random Nearest Neighbour Solution")
    loop_variable = runs
    for i in range(loop_variable):
        random_sp = r.choice(list(cities.keys()))
        route = TSPSolutionNearestNeighbour(distance, paths, random_sp)
        f = open(output_filename, 'a')
        f.write("In Run:" + str(i+1) + ", the random starting point is:" + str(random_sp) + "\n")
        f.close()
        printOutputFile(route, output_filename)
    return


def printOutputFile(travel_path, output_filename):
    sp_len = len(travel_path)
    # print("sp_len: ", sp_len)
    with open(output_filename, 'a') as f:
        for i in range(sp_len):
            line = str(travel_path[i, 0]) + "\t" + str(travel_path[i, 1]) + "\t" + str(travel_path[i, 2])
            # print(line)
            f.write(line)
            f.write('\n')
        f.write('=============================\n')

# Main call
if __name__ == '__main__':

    start_time = t.time()
    # Read input data file with co-ordinates
    paths = readInputFile("inst-0.tsp")

    # Find the distance between all pairs of cities
    dist = distanceBetweenCities(paths)
    # print("Printing distance between cities :\n", dist)

    # Find the route using the shortest neighbour logic by visiting each city once
    # short_path = TSPSolutionNearestNeighbour(dist, paths, 1)
    # print("Printing final solution inside main :\n", short_path)
    # printOutputFile(short_path, 'nearest_neighbour_output.txt')

    # Find routes starting from random starting city and traversing through the nearest city
    # Visit all cities only once
    TSPSolutionRandom(distance=dist, paths=paths, runs=100, output_filename='random_output_0.txt')
    # printOutputFile(random_routes, 'random_output.txt')

    end_time = t.time()
    elapsed_time = end_time - start_time
    print("Elapsed Time: ", elapsed_time)
