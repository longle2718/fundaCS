# Bellman-Ford algorithm
#
# Long Le <longle1@illinois.edu>
# University of Illinois
#
import numpy as np
from pqdict import minpq

def bellman_ford(aMap,start,goal):
    M,N = np.shape(aMap)

    # dict/map, for storing results
    dist = {}
    prev = {} 

    # Step 1: initialization
    for m in range(M):
        for n in range(N):
            node = (m,n)
            if node == start:
                dist[node] = 0
            else:
                dist[node] = np.infty

    # Step 2: relaxation
    edges = getEdges(M,N)
    for i in range(M*N-1):
        for e in edges:
            u = e[0]
            v = e[1]
            w = getDist(u,v,aMap)
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u

    # Step 3: check for negative-weight cycles
    for e in edges:
        if dist[u] + w < dist[v]:
            print('Negative-weight cycles detected')
            return None,None

    return getPath(goal,prev),dist[goal]

def getPath(cur,prev):
    fullPath = []
    fullPath.append(cur)
    while cur in prev:
        cur = prev[cur]
        fullPath.append(cur)

    return fullPath

def getEdges(M,N):
    edges = []
    for m in range(M):
        for n in range(N):
            node = (m,n)
            ngb = getNeighbor(node,M,N)
            for n in ngb:
                if (node,n) not in edges and (n,node) not in edges:
                    edges.append((node,n))

    return edges
    
def getDist(u,v,aMap):
    # get the exact dist
    if aMap[u] == 1 or aMap[v] == 1:
        return np.infty

    return np.linalg.norm(np.array(u)-np.array(v))

def getNeighbor(node,M,N):
    ngb = []
    for d in [[0,1],[1,0],[1,1],[0,-1],[-1,0],[-1,-1],[1,-1],[-1,1]]:
        # list and dict just append elements, only np.array adds/mults element-wise
        n = tuple(np.array(node)+d) 
        if n[0]>=0 and n[0]<M and n[1]>=0 and n[1]<N:
            ngb.append(n)

    return ngb
