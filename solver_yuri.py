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
        centers[i] = cities[i*n]           #どの座標でも良い
    return centers

def calc_new_centers(group,n,N,cities):
    newcenters = [() for i in range(n)]
    for i in range(n):
        sum = [0 for i in range(2)]
        for s in range(len(group[i])):    #重心を測定
            sum[0] += cities[group[i][s]][0]/(len(group[i]))
            sum[1] += cities[group[i][s]][1]/(len(group[i]))
        newcenters[i]=tuple(sum)          #[(g1_x,g1-y),(g2_x,g2-y),,,,,,]
    return newcenters

def make_group(centers,cities,n,N):
    group =[[] for i in range(n)]
    for t in range(N):
        min_dis = 1000000
        group_num = 0
        for l in range(n):                #ある都市から見て最も近い重心を決める
            if(min_dis >distance(centers[l],cities[t])):
                min_dis = distance(centers[l],cities[t])
                group_num = l;
        group[group_num].append(t)
    return group

#kmeans法によって点を近い点同士でグループ化する
#一番最初に動く関数
def kmeans(cities):
    N = len(cities)
    n = (int)(math.sqrt(N))
    dist = [[0] * N for i in range(N)]
   
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
  
    centers = [[0 for k in range(2)] for i in range(n)]
    centers = initcenters(centers,n,cities)             #初期重心リスト決定[[x][y],[x][y],[x][y],,,,]

    for s in range(10):
        groups = make_group(centers,cities,n,N)         #重心に対して近い点でグループが作られたリスト
        newcenters = calc_new_centers(groups,n,N,cities)#重心の再計算
        centers = newcenters                            #10回K-meansを行う
         # print("newcenters")
         # print(newcenters)
    return groups,newcenters
    


#ある1groupに対してgreedyな経路を作成する
def solve(group,cities):
    grouptup = tuple(group)
    N = len(grouptup)
    current_city = grouptup[0]
    unvisited_cities = set(grouptup[1:])#TypeError: unhashable type: 'list'
    solution = [current_city]

    def distance_from_current_city(to):
        return distance(cities[current_city],cities[to])

    while unvisited_cities:
        next_city = min(unvisited_cities, key=distance_from_current_city)
        unvisited_cities.remove(next_city)
        solution.append(next_city)
        current_city = next_city
    return solution

#centersはcitiesと同じ[(x_1,y_1),(x_2,y_2),,,]
def making_centerlist(centers,cities):
    center_solution =[]
    kcenter = kmeans(centers)[0]#kcenter =[[0,2,7],[1,3,4,5,6],,,]
   
    for l in range(len(kcenter)):#1 way
       center_solution.extend(kcenter[l])#1way
    #center_solution.extend(solve(kcenter, centers))#2way#Error
    print("center_solution")
    print(center_solution)
    return center_solution

#各グループで作られた経路を合併させる
def solutionplus(groups,cities,centers):
    solution = [0]
    center_list = making_centerlist(centers,cities)#各グループ重心のgreedy経路
    #print("center_list")
    #print(center_list)
    for i in range(len(groups)):
        k = center_list[i]#各グループの中心点のgreedy経路の順に並べる
        solution += solve(groups[k],cities)
    return solution
    

if __name__ == '__main__':
    assert len(sys.argv) > 1
    cities = read_input(sys.argv[1])
    groups = kmeans(cities)[0]
    centers = kmeans(cities)[1]
    print("groups")
    print(groups)
    print("centers")
    print(centers)
    solution = solutionplus(groups,cities,centers)
    print_solution(solution)
