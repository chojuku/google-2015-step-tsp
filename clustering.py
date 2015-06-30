#!/usr/bin/env python3
#coding:UTF-8
import sys
import math
import random
import numpy as np
from sklearn.cluster import KMeans

from common import print_solution, read_input

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):
    N = len(cities)
    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
    n =(int)(math.sqrt(N))
    #features = np.array(cities)
    for i in  range(2):
        print (cities)
        
    codebook, destortion = scipy.cluster.vq.kmeans(cities, n, iter=20, thresh=1e-05)
    print (codebook, destortion)
#    kmeans_model=KMeans(n_cluster=n,random_state =10).fit.(cities)
    #labels = kmeans_model.labels_
    #for label, city in zip(labels, cities):
     #   print (label, citiy)

#
"""
    current_city = 0
    unvisited_cities = set(range(1, N))
    solution = [current_city]
    

    def distance_from_current_city(to):#dont change indent!
        return dist[current_city][to]

    while unvisited_cities:
        next_city = min(unvisited_cities, key=distance_from_current_city)
        unvisited_cities.remove(next_city)
        solution.append(next_city)
        current_city = next_city
    return solution

#def merge(solutions):
    """

if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
   # means = kmeans(read_input(sys.argv[1]))
  #  solution = solve(means)
   # solution += solve(means)
    print_solution(solution)
