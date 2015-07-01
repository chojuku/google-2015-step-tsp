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
        centers[i] = cities[i*n]
    return centers

def calc_new_centers(group,n,N,cities):
    newcenters = [() for i in range(n)]
    for i in range(n):
        sum = [0 for i in range(2)]
        for s in range(len(group[i])):
            sum[0] += cities[group[i][s]][0]/(len(group[i]))
            sum[1] += cities[group[i][s]][1]/(len(group[i]))
        newcenters[i]=tuple(sum)
    return newcenters

def make_group(centers,cities,n,N):
    group =[[] for i in range(n)]
    for t in range(N):
        min_dis = 1000000
        group_num = 0
        for l in range(n):
            if(min_dis >distance(centers[l],cities[t])):
                min_dis = distance(centers[l],cities[t])
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

    #for i in range(n):
        #print (centers[i])
    for s in range(10):
        group = make_group(centers,cities,n,N)
        newcenters = calc_new_centers(group,n,N,cities)
        #print("newcenters")
       # print(newcenters)
        #if(distance(cities[centers],cities[newcenters])<0.5):
         #   break
        centers = newcenters
    return group
    



def solve(group,cities):
    grouptup = tuple(group)
    N = len(grouptup)
    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[grouptup[i]], cities[grouptup[j]])
    current_city =0
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

def solutionplus(group,cities):
    solution = [0]
    for i in range(len(group)):
        solution += solve(group[i],cities)
    return solution

#def merge(solutions):
    

if __name__ == '__main__':
    assert len(sys.argv) > 1
    #solution = solve(read_input(sys.argv[1]))
    cities = read_input(sys.argv[1])
    group = kmeans(cities)
    print("group")
    print(group)
    solution = solutionplus(group,cities)
    print_solution(solution)
