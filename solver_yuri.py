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
    return groups
    


#ある1groupに対してgreedyな経路を作成する
def solve(group,cities):
    grouptup = tuple(group)                            
    N = len(grouptup)
    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[grouptup[i]], cities[grouptup[j]])
    #current_city = 0                            #current_city =0 unvisited_cities =set(1,range(N))実行されるが間違った経路となる
    #unvisited_cities =set(1,range(N))        
    current_city = grouptup[0]                  #正しいのはこちらのはずだが distance_from_current_cityでIndexError: list index out of range
    unvisited_cities = set(grouptup)
    solution = [current_city]
    #print("unvisited_cities_before_while =")
    #print(unvisited_cities)


    def distance_from_current_city(to):#dont change indent!
        return dist[current_city][to]

    while unvisited_cities:
        next_city = min(unvisited_cities, key=distance_from_current_city)
        unvisited_cities.remove(next_city)
        #print("unvisited_cities_in_while")
        #print(unvisited_cities)
        solution.append(next_city)
        current_city = next_city
    return solution


def solutionplus(groups,cities):
    solution = [0]
    for i in range(len(groups)):
        solution += solve(groups[i],cities)
    return solution

#Not Complete　未完成
def merge(groups,cities):
    N = len(cities)
    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])


#あるグループ内のある点とその他すべての点の中で最も最短をとる点の組と２番目の組を出力
    for k in range(len(groups)):
        for i in range(len(groups[k])):
            min_dis = 1000000
            for j in range(len(cities)):
                for s in range(len(groups[k])):
                    if(min_dis >dist[groups[k][i]][j] and j != groups[k][s]):
                        second_mergepoint = mergepoint
                        min_dis = dist[groups[k][i]][j]
                        mergepoint =(groups[k][i], [j])
    
        #solution = solve(groups[k],cities) #計算量が気に入らないのでこの方針は模索中
    


if __name__ == '__main__':
    assert len(sys.argv) > 1
    #solution = solve(read_input(sys.argv[1]))
    cities = read_input(sys.argv[1])
    groups = kmeans(cities)
    print("groups")
    print(groups)
    solution = solutionplus(groups,cities)
    print_solution(solution)
