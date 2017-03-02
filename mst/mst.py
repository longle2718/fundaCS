# Minimum spanning tree (MST) algorithms
#
# Long Le
# University of Illinois
#

import numpy as np
import matplotlib.pyplot as plt
from pqdict import minpq

class Node:
    def __init__(self,x):
        self.val = x

class Edge:
    def __init__(self,n0,n1,w):
        self.ePts = set([n0,n1]) # end points
        self.w = w # weight

def Prim(nodes,edges):
    # https://en.wikipedia.org/wiki/Prim's_algorithm
    C = minpq() # cheapest cost of a connection to a node
    E = {} # the edge providing that cheapest connection
    for node in nodes:
        C[node] = np.infty
        E[node] = None
    F = set() # forest

    while len(C) > 0:
        node = C.pop()

        nodeNew = Node(node.val)
        if E[node] != None:
            nodeNew.edges[E[node]] 
        F.add(nodeNew)

        for ngb in node.edges.keys():
            if ngb in C:
                if node.edges[ngb] < C[ngb]:
                    C[ngb] = node.edges[ngb]
                    E[ngb] = node

    return F

def Kruskal(nodes,edges):
    # https://en.wikipedia.org/wiki/Kruskal's_algorithm
    return

def visualize(nodes,edges,locMap):
    plt.figure(figsize=(10,10))
    for node in nodes:
        loc = locMap[node]
        plt.scatter(loc[0],loc[1],lw=32)
        plt.annotate(str(node.val),xy=loc,xytext=(loc[0]+.1,loc[1]+.1),fontsize=15)
    for edge in edges:
        loc = []
        for ePt in edge.ePts:
            loc.append(locMap[ePt])
        #print('loc = %s' % loc)
        add_label(plt.plot([loc[0][0],loc[1][0]],[loc[0][1],loc[1][1]])[0],'%.2f' % edge.w)

    axes = plt.axes()
    axes.axison=False
    plt.show()
    return

def add_label(line,label,size=20,color=None):
    if color is None:
        color = line.get_color()

    xdata = line.get_xdata()
    ydata = line.get_ydata()
    xStart = np.percentile(xdata,55)
    xEnd = np.percentile(xdata,45)
    yStart = np.percentile(ydata,55)
    yEnd = np.percentile(ydata,45)

    line.axes.annotate(label,
            xy=((xEnd+xStart)/2,(yEnd+yStart)/2),size=18)
