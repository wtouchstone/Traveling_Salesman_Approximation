import numpy as np
from collections import defaultdict 
from random import *
import sys
import time
nodes = list()
edges = list()
mst = list()
infile = sys.argv[1]
outfile = sys.argv[2]
totaltime = float(sys.argv[3])
def euclid(node1, node2):
    return pow(pow((node1[0] - node2[0]), 2) + pow((node1[1] - node2[1]), 2), .5)

def setup(file):
    file = open(file)
    for i in file.readlines():
        nodes.append((float(float(i.split()[1])), float(float(i.split()[2]))))
    for i in range(len(nodes)):
        edges.append(list())
        for j in range(len(nodes)):
            edges[i].append((    euclid(nodes[i], nodes[j]), 0, (i, j)    ))
setup(infile)

closest = [-1]*len(nodes)

for i in range(len(closest)):
    closest[i] = list()
    for j in range(len(closest)):
        if i != j:
            temp = euclid(nodes[i], nodes[j])
            closest[i].append((float(temp), j)) 
    closest[i].sort()

# Picks the nearest node to the current node.

def pickNearest(curr, visited):
    mindist = float('inf')
    nearest = -1
    for i in range(len(nodes)-1):
        if closest[curr][i][1] not in visited:
            distance = closest[curr][i][0]
            pheremone = edges[curr][closest[curr][i][1]][1]
            if ( distance - pheremone  < mindist):
                mindist = distance - pheremone
                nearest = closest[curr][i][1]
    return nearest

# This will perform a completely random walk in the graph with no considerations for distances.

def randomWalk():
    start = randrange(len(nodes))
    path = list()
    path.append(start)
    visited = set()
    visited.add(start)
    curr = start
    while len(visited) < len(nodes):
        nextup = pickNearest(curr, visited)
        visited.add(nextup)
        path.append(nextup)
        curr = nextup
    path.append(start)
    return path    

# Updates the paths between nodes when a run of ants concludes. Modify pheromone_weight to determine the amount by which the path
# is modified.

def update(path, mincost, newmincost):
    for i in range(1, len(path)):
        prenode = path[i-1]
        node = path[i]
        pheromone_weight = 1.00
        edges[prenode][node] = (edges[prenode][node][0], edges[prenode][node][1] + (mincost - newmincost * pheromone_weight), edges[prenode][node][2])

# Returns the cost os a path        

def cost(path):
    total = 0
    for i in range(1, len(path)):
        prenode = path[i-1]
        node = path[i]
        total += edges[prenode][node][0]
    return total

# This will simulate a numiters amount of ants that will base their movements off 
# their nearest neighbor and the pheremone trail that currently exists.

def simants(numiters):
    mincost = float('inf')
    minwalk = None
    for i in range(numiters):
        if (time.time() - start >= totaltime):
            f.writelines('Cost: ' + str(cost(absbestpath)) + '\nPath: ' + str(absbestpath) + '\n')
            quit()   
        walk = randomWalk()
        c = cost(walk)
        if c < mincost:
            minwalk = walk
            mincost = c
    print("simmed")
    return (mincost, minwalk)


f = open(outfile, 'w')
start = time.time()
absbestcost = float('inf')
absbestpath = None

# This will run the algorithm for as long a time as it is provided.

while True:
    if (time.time() - start >= totaltime):
        f.writelines('Cost: ' + str(cost(absbestpath)) + '\nPath: ' + str(absbestpath) + '\n')
        quit()
    baseline = simants(20)
    best = baseline
    baseline = (baseline[0] + 100, baseline[1])
    prior = Nonebest = baseline
    pre = time.time()
    for i in range(100):
        new = simants(100)
        update(new[1], baseline[0], new[0])
        if new[0] < best[0]:
            best = new
    post = time.time()
    print(best[1])
    print(cost(best[1]))
    if (cost(best[1]) < absbestcost):
        absbestcost = cost(best[1])
        absbestpath = best[1]
    
f.writelines('Cost: ' + str(cost(absbestpath)) + '\nPath: ' + str(absbestpath) + '\n')

f.close()
