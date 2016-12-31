# Various Dijkstra-based algorithm for solving the shortest path problem
#
# Long Le <longle1@illinois.edu>
# University of Illinois
#
import numpy as np
from pqdict import minpq

def dijkstra(aMap,start,goal):
    # basic, priority-queue version
    M,N = np.shape(aMap)

    # the queue of all untouched nodes
    # dict/map with queue features (pop/additem)
    # smaller value has higher priority
    qDist = minpq() 
    # dict/map
    prev = {} 
    for m in range(M):
        for n in range(N):
            if [m,n] == start:
                qDist[(m,n)] = 0
            else:
                qDist[(m,n)] = np.infty
            prev[(m,n)] = np.nan

    while len(qDist) > 0:
        u = qDist.pop()
        if u == goal:
            return getPath(u,prev) 
        for v in getNeighbor(u,M,N):
            if v in qDist:
                alt = qDist[u] + getDist(u,v)
                if alt < qDist[v]:
                    qDist[v] = alt
                    prev[v] = u
    
    return None

def dijkstra_ucs(aMap,start,goal):
    # uniform cost search

    return None

def Astar(aMap,start,goal):
    # A* improvement

    return None

def getPath(cur,prev):
    fullPath = []
    fullPath.append(cur)
    while cur in prev:
        cur = prev[cur]
        fullPath.append(cur)

    return fullPath

def getDist(u,v):
    return np.linalg.norm(np.array(u)-np.array(v))

def getNeighbor(node,M,N):
    ngb = []
    delta = [[0,1],[1,0],[1,1],[0,-1],[-1,0],[-1,-1],[1,-1],[-1,1]]
    for d in delta:
        n = list(node)+d
        if n[0]>=0 and n[0]<M and n[1]>=0 and n[1]<N:
            ngb.append(tuple(n))

    return ngb

