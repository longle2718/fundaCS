# Various Dijkstra-based algorithm for solving the shortest path problem
#
# Long Le <longle1@illinois.edu>
# University of Illinois
#
import numpy as np
from pqdict import minpq

def dijkstra(aMap,start,goal):
    # basic, priority-queue version: only works for finite maps
    M,N = np.shape(aMap)

    # dict/map, for storing results
    dist = {}
    prev = {} 
    # one queue of all untouched nodes (hence only need to dequeue)
    # dict/map with queue features (pop/additem)
    # smaller value has higher priority
    unexplored = minpq() 

    for m in range(M):
        for n in range(N):
            node = (m,n)
            if node == start:
                unexplored[node] = 0
            else:
                unexplored[node] = np.infty

    while len(unexplored) > 0:
        # dequeue
        node,minD = unexplored.popitem()
        #print('node = '+str(node))
        dist[node] = minD
        if node == goal:
            #print('dist = '+str(dist))
            #print('prev = '+str(prev))
            return getPath(node,prev),dist[node]

        # visit neighbors
        for ngb in getNeighbor(node,M,N):
            #print('ngb = '+str(ngb))
            if ngb in unexplored:
                alt = dist[node] + getDist(node,ngb,aMap) # node is already out of unexplored
                if alt < unexplored[ngb]:
                    #print('alt = '+str(alt))
                    unexplored[ngb] = alt
                    prev[ngb] = node
    
    return None

def dijkstra_ucs(aMap,start,goal):
    # uniform cost search: works for inf maps
    M,N = np.shape(aMap)

    # dict/map, for storing results
    dist = {}
    prev = {} 
    # two queues: 
    # a queue of growing/incomplete untouched nodes
    frontier = minpq()
    # a queue of visited nodes
    explored = []

    frontier[start] = 0

    while True:
        if len(frontier) == 0:
            return None

        # dequeue
        node,minD = frontier.popitem()
        dist[node] = minD
        #print('minD = '+str(minD))
        if node == goal:
            return getPath(node,prev),dist[node]

        explored.append(node)

        # visit neighbors
        for ngb in getNeighbor(node,M,N):
            #print('ngb = '+str(ngb))
            if ngb not in explored:
                if ngb not in frontier:
                    frontier[ngb] = np.infty # new frontier

                alt = dist[node] + getDist(node,ngb,aMap)
                if alt < frontier[ngb]:
                    frontier[ngb] = alt
                    prev[ngb] = node

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

def getDist(u,v,aMap):
    if aMap[u] == 1 or aMap[v] == 1:
        return np.infty

    return np.linalg.norm(np.array(u)-np.array(v))

def getNeighbor(node,M,N):
    ngb = []
    delta = [[0,1],[1,0],[1,1],[0,-1],[-1,0],[-1,-1],[1,-1],[-1,1]]
    for d in delta:
        n = np.array(node)+d # list and dict just append elements, only np.array adds/mults element-wise
        if n[0]>=0 and n[0]<M and n[1]>=0 and n[1]<N:
            ngb.append(tuple(n))

    return ngb

