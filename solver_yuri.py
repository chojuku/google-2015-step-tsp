#!/usr/bin/env python3
#coding:UTF-8
import sys
import math
import random

from common import print_solution, read_input

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def initcenters(centers,n,cities):
    for i in range(n):
        centers = [random.uniform(0,1600.0)][random.uniform(0,900.0)]
        #centers[i] = cities[i*n]
    return centers

def calc_new_centers(group,n,N,cities):
    newcenters = [[0 for k in range(2)] for i in range(n)]
    while(group[l] != []):
        group[l][
    for t in range(N):
        for i in range(n):
            sum[i] += (group[i][])**2
             
    newcenters[i] = (sum[i] / n)  + centers[i]        
    return newcenters

def make_group(centers,cities,n,N):
    group =[[0] for i in range(n)]
        for t in range(N):
            min_dis = min(distance(centers[0],cities[t]))
            group_num = 0
            for l in range(n):
                if(min_dis >min(distance(centers[l],cities[t])):
                   min_dis = min(distance(centers[l],cities[t]))
                   group_num = l;
            group[group_num].append(t)
    return group


def kmeans(cities):
    N = len(cities)    
    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
    n = (int)(math.sqrt(N))
    centers = [[0 for k in range(2)] for i in range(n)]
    centers = initcenters(centers,n,cities)
    for i in range(n):
        print centers
    for s in range(100):
        group = make_group(centers,cities,n,N)
        newcenters = calc_new_centers(group,n,N,cities)
        if(distance(centers,newcenters)<0.5):
            break
        cuenters = newcenters
    return g
    



def solve(cities):
    N = len(cities)
    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
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
    

if __name__ == '__main__':
    assert len(sys.argv) > 1
    #solution = solve(read_input(sys.argv[1]))
    means = kmeans(read_input(sys.argv[1]))
    solution = solve(means)
   # solution += solve(means)
    print_solution(solution)
