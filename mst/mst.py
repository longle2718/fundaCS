# Minimum spanning tree (MST) algorithms
#
# Long Le
# University of Illinois
#

import numpy as np
import matplotlib.pyplot as plt

class Node:
    def __init__(self,x):
        self.val = x
        self.edges = {}

def Prim(nodes):
    # https://en.wikipedia.org/wiki/Prim's_algorithm
    C = {}
    for node in nodes:
        C[node] = np.infty
    E = {}
    for node in nodes:
        E[node] = None

    F = set()
    Q = 
    F.add(nodes[0])
    for node in tree:


    return tree

def Kruskal(nodes):
    # https://en.wikipedia.org/wiki/Kruskal's_algorithm
    return

def visualize(nodes,locMap):
    plt.figure(figsize=(10,10))
    for node in nodes:
        loc = locMap[node]
        plt.scatter(loc[0],loc[1],lw=32)
        plt.annotate(str(node.val),xy=loc,xytext=(loc[0]+.1,loc[1]+.1),fontsize=15)
        for ngb in node.edges.keys():
            locNgb = locMap[ngb]
            plt.plot([loc[0],locNgb[0]],[loc[1],locNgb[1]])

    axes = plt.axes()
    axes.axison=False
    plt.show()
    return
