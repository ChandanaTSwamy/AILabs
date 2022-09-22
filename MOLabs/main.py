# Travelling Salesman Problem

# from itertools import islice

import random


# Test GIT
def TSPSolution ():
    readInputFile("inst-21.tsp")

def distanceBetweenCities(city):
    pass

def readInputFile(input_file):
    cities = {}

    with open(input_file) as filearr:
        paths = int(filearr.readline())
        print('No.of paths: ', paths)

        for i in range(paths):
            linearr = filearr.readline()
            # print(linearr.split())
            splittxt = linearr.split()
            print(splittxt)
            cities[int(splittxt[0])] = (int(splittxt[1]), int(splittxt[2]))

    print(cities)
    return cities


distanceBetweenCities (city):
    # w(u, v) = nint(sqrt((x(u) - x(v)) ^ 2 + (y(u) - y(v)) ^ 2))

