import numpy as np
from collections import defaultdict 
nodes = list()
edges = list()
mst = list()

class node():
    def __init__(self, num):
        self.num = num
        self.children = list()
    num = -1
    children = list()
    def __str__(self):
        return str(self.num) + ' ' + str(self.children)

  






def euclid(node1, node2):
    return pow(pow((node1[0] - node2[0]), 2) + pow((node1[1] - node2[1]), 2), .5)

def setup(file):
    file = open(file)
    for i in file.readlines():
        nodes.append((int(float(i.split()[1])), int(float(i.split()[2]))))
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if i != j:
                edges.append((euclid(nodes[i], nodes[j]), (i, j)))
    edges.sort()

setup("mat-test.txt")

edgedup = edges.copy()


def treeify(nodes):
    mstdup = mst.copy()
    nodelist = list()
    for i in mstdup:
        curr = node(i[0])
        curr.children.append(i[1])
        print(curr)
        nodelist.append(curr)
    print(nodelist)
    for i in range(len(nodelist)):
        try:
            curr = nodelist[i]
        except:
            break
        for j in range (len(nodelist)):
            if curr.num == nodelist[j].num:
                for child in nodelist[j].children:
                    curr.children.append(child)
                del nodelist[j]
    return nodelist

order = list()
def edgelist2adjlist(inlist):
    adjList = [0] * len(nodes)
    for i in range(len(nodes)):
        adjList[i] = list()
        for item in inlist:
            if item[0] == i:
                adjList[i].append(item[1])
    return adjList




def kruskalls():
    treenodes = set()
    while len(treenodes) < len(nodes):
        if not ((edgedup[0][1][0] in treenodes) and (edgedup[0][1][1] in treenodes)):
            mst.append(edgedup[0][1])
            treenodes.add(edgedup[0][1][0])
            treenodes.add(edgedup[0][1][1])
            del edgedup[0]
            mst.append(edgedup[0][1])
            del edgedup[0]
        else:
            del edgedup[0]
            del edgedup[0]  
    print(mst)

def traverse(inlist):
    print(inlist)
    order = list()
    stack = list()
    visited = set()
    curr = 0
    while True:
        for i in inlist[curr]:
            if i not in visited:
                stack.append(i)
        print(stack)
        order.append(curr)
        visited.add(curr)
        if len(stack) == 0:
            break
        curr = stack.pop()
        
    return order



            
                     
kruskalls()


#print(mst)

#print(mst)
adjlist = edgelist2adjlist(mst)
traverse(adjlist)





def cost(path):
    cost = 0
    for i in range(len(path) - 1):
        cost += euclid(path[i], path[i+1])
    return cost

temp = 0

def nn(nodein):
    sequence = list()
    sequence.append(nodein)
    visited = set()
    visited.add(nodein)
    curr = nodein
    while (len(sequence) < len(nodes)):
        mindist = float('inf')
        nearest = None
        for node in nodes:
            if node not in visited:
                if (euclid(curr, node) < mindist):
                    mindist = euclid(curr, node)
                    nearest = node
        sequence.append(nearest)
        visited.add(nearest)
        curr = nearest
    sequence.append(nodein)
    return sequence

def allNN():
    minCost = float('inf')
    minpath = None
    for node in nodes:
        currsequence = nn(node)

        currcost = cost(currsequence)
        if currcost < minCost:
            minCost = currcost
            minpath = currsequence
    return minCost


            

temp = allNN()

#for node in temp:
#    print(nodes.index(node) + 1)
