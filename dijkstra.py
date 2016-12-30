# Various Dijkstra-based algorithm for solving the shortest path problem
#
# Long Le <longle1@illinois.edu>
# University of Illinois
#
import numpy as np
import queue

define dijkstra(aMap,src):
    # basic, priority-queue version
    M,N = np.shape(aMap)

    unexploredQ = queue.PriorityQueue() # inf queue of unexplored nodes
    dist = {}
    prev = {}
    for m in range(M)dd:
        for n in range(N):
            if [m,n] == src:
                dist[(m,n)] = 0
            else:
                dist[(m,n)] = np.infty
            prev[(m,n)] = np.nan
            unexploredQ.put((dist[(m,n)],[m,n]))

    while !unexploredQ.empty():
        u = unexploredQ.get()
        for n in getNeighbor(u):
            if vecExist(n,unexploredQ.queue):
                alt = dist[tuple(u)] + getDist(u,v)
                if alt < dist[tuple(v)]:
                    dist[tuple(v)] = alt
                    prev[tuple(v)] = u
    
    return None

define dijkstra_ucs(aMap,src):
    # uniform cost search

    return None

define Astar(aMap,src):
    # A* improvement

    return None

def getDist(u,v):
    return np.linalg.norm(u-v)

def getNeighbor(src,M,N):
    ngb = []
    delta = [[0,1],[1,0],[1,1],[0,-1],[-1,0],[-1,-1],[1,-1],[-1,1]]
    for d in delta:
        n = src+d
        if n[0]>=0 and n[0]<M and n[1]>=0 and n[1]<N:
            ngb.append(n)

    return ngb

def vecExist(vec,aQueue):
    for vecQ in aQueue:
        if vec == vecQ: # assume list, not np.array
            return True

    return False
