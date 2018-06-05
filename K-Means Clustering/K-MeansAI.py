#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 11:57:12 2018

@author: paragasa
"""
#imports
import pandas as pd
from math import sqrt
import numpy as np
import copy

# Importing the dataset
dataset = pd.read_csv('DSAI4.csv')
X3 = dataset.iloc[:, 2:5].values
oldcentroids =[[0 for x in range(K)] for y in range(K)] #list of centroid to print
currentcentroids = [[0 for x in range(K)] for y in range(K)]
#clusters
K= 3

"""  
Distance from x dataset and  y cluster
"""
def distance_func(x,y):
    clustClosest = 3
    distanceClose = 1000
    for i in range(len(y)):
        val= (x[0]- y[i][0])**2 + (x[1]- y[i][1])**2 + (x[2]- y[i][2])**2
        val = sqrt(val)
        if(val < distanceClose):
            distanceClose= val
            clustClosest = i
    return clustClosest
#tscenter = randomCenters(X3)
#ts= distance_func(X3[80],tscenter)

"""
will get centroids random centroid points
"""
def randomCenters(x):
    retCentroids= [[0 for x in range(K)] for y in range(K)] 
    for n in range(K):
        random = np.random.randint(0,len(x))
        retCentroids[n][0]= x[random][0]
        retCentroids[n][1]= x[random][1]
        retCentroids[n][2]= x[random][2]
        print(retCentroids)
    return retCentroids

"""
Kmeans alg will randomize centers for clusters
1. will continously loop till old centroids will be equal to current centroids
2.Each point of dataset will be deducted from each cluster, the least difference is grouped with cluster
3. average is made for each attribute, avergae for each attriubte attained
4. remake clusters 
"""
def Kmeans(X):
    oldcentroids = randomCenters(X)
    print("========Randomoized Centers for Clusters================")
    print( oldcentroids)
    done= False # false till centroids are equal
    t=1 #count iterations
    while(done != True):
        clusters= [[0 for x in range(K)] for y in range(K)]
        cluster_count = [0,0,0]
        print("Iteration:")
        print(t)
        t += 1 
        for i in range(len(X)):
            d = distance_func(X[i],oldcentroids)
            clusters[d][0] += X[i][0]
            clusters[d][1] += X[i][1]
            clusters[d][2] += X[i][2]
            cluster_count[d] += 1
           
        for j in range(0,K):
            currentcentroids[j][0] = clusters[j][0]/ cluster_count[j]
            currentcentroids[j][1] = clusters[j][1]/ cluster_count[j]
            currentcentroids[j][2] = clusters[j][2]/ cluster_count[j]
            print("=========Information for Cluster " + str(j) + "==================")
            print("averages for 3,4,5: " +  "{0:.4f}".format(currentcentroids[j][0]) + "|" + "{0:.4f}".format(currentcentroids[j][1]) + "|" + "{0:.4f}".format(currentcentroids[j][2])  )
#            print(currentcentroids[j])
        print("==============Clustor SUM===============================")
        print (clusters)
        print("=============Clustor Count============================")
        print(cluster_count)
        if(oldcentroids == currentcentroids):
            print("old centroids")
            print(oldcentroids)
            print(" is equal to current")
            print(currentcentroids)
            done = True
        else:
            print("old centroids")
            print(oldcentroids)
            print(" Current is")
            print(currentcentroids)
            
        oldcentroids = copy.deepcopy(currentcentroids)

"""
EXECUTE:
"""        
Kmeans(X3)
                