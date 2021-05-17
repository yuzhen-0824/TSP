# -*- coding: utf-8 -*-
"""
Created on Mon May 17 11:02:06 2021

@author: User
"""

#create graph
import random

def Graph(n):
    matrix = [([0] * n) for i in range(n)] 
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = 0
            else:
                matrix[i][j] = random.randrange(1, 30)
    return matrix

#dynamic programming
import copy 
def TSP_DP(k, a):
    if (k, a) in g:
        # Already calculated Set g[%d, (%s)]=%d' % (k, str(a), g[k, a]))
        return g[k, a]
    values = []
    all_min = []
    for j in a:
        set_a = copy.deepcopy(list(a))
        set_a.remove(j)
        all_min.append([j, tuple(set_a)])
        result = TSP_DP(j, tuple(set_a))
        values.append(matrix[k-1][j-1] + result)
    # get minimun value from set as optimal solution for
    g[k, a] = min(values)
    p.append(((k, a), all_min[values.index(g[k, a])]))
    return g[k, a]

#naive approach
from sys import maxsize
from itertools import permutations
def TSP_NA(graph, s, V):
    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
    # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation=permutations(vertex)
    for i in next_permutation:
        # store current Path weight(cost)
        current_pathweight = 0
        # compute current path weight
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
        # update minimum
        min_path = min(min_path, current_pathweight)
    return min_path

#main function
import time
import csv
g = {}
p = []
l = []
a = ()
for V in range(4, 21): 
    print("vertex number: ", V)
    matrix = Graph(V)
    for x in range(1, V):
        g[x + 1, ()] = matrix[x][0]
        l.append(x+1)
        a = tuple(l)
    #run TSP_DP
    start = time.time()
    r1 = TSP_DP(1, a)
    end = time.time()
    time1 = end-start
    print("DP_weight:", r1, "; DP_time:", time1)
    #run TSP_NA
    start = time.time()
    r2 = TSP_NA(matrix, 0, V)
    end = time.time()
    time2 = end-start
    print("NA_weight:", r2, "; NA_time:", time2)
    #calculate error
    error = (r2 - r1)/r1
    print("error:", error)
    print("-------------------------------------------------")
    with open('TSP_data1.csv', 'a+', newline='')as csvFile:        
        csvWriter = csv.writer(csvFile)
        #csvWriter.writerow(['vertex number', 'dp weight','na weight','dp_time', 'na_time', 'error'])
        csvWriter.writerow([str(V), str(r1), str(r2), str(time1), str(time2), str(error)])    
    csvFile.close()