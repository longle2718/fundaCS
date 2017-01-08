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
    # one priority (a dict/map hybrid with queue features, i.e. pop/additem) queue 
    # of all untouched nodes (hence only need to dequeue)
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
        dist[node] = minD
        #print('dist[node]= '+str(dist[node]))
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
    
    return None,None

def dijkstra_ucs(aMap,start,goal):
    # uniform cost search: works for inf maps
    M,N = np.shape(aMap)

    # dict/map, for storing results
    dist = {}
    prev = {} 
    # two queues: 
    # a priority (dict-hybrid) queue of growing/incomplete untouched nodes
    frontier = minpq()
    # a queue of visited nodes
    #explored = []
    explored = set()

    frontier[start] = 0

    while len(frontier) > 0:
        # dequeue
        node,minD = frontier.popitem()
        dist[node] = minD
        #print('dist[node]= '+str(dist[node]))
        if node == goal:
            return getPath(node,prev),dist[node],explored

        # enqueue
        #explored.append(node)
        explored.add(node)

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

    return None,None,explored

def Astar(aMap,start,goal):
    # A* improvement: works for inf maps and efficient
    M,N = np.shape(aMap)

    # dict/map, for storing results
    dist = {} # mutable in A*
    prev = {}
    # two queues: 
    # a priority (dict-hybrid) queue of growing/incomplete untouched nodes
    frontier = minpq()
    # a queue of visited nodes
    explored = set()

    frontier[start] = 0+getHeuristic(start,goal)
    dist[start] = 0

    while len(frontier) > 0:
        # dequeue
        node = frontier.pop()
        #print('dist[node]= '+str(dist[node]))
        # dist.get(node,np.infty) is equivalent to dist[node] with the default value of np.infty 
        if node == goal:
            return getPath(node,prev),dist[node],explored

        # enqueue
        explored.add(node)

        # visit neighbors
        for ngb in getNeighbor(node,M,N):
            #print('ngb = '+str(ngb))
            if ngb not in explored:
                if ngb not in frontier:
                    frontier[ngb] = np.infty # new frontier
                    dist[ngb] = np.infty

                alt = dist[node] + getDist(node,ngb,aMap)
                if alt < dist[ngb]:
                    frontier[ngb] = alt+getHeuristic(ngb,goal)
                    dist[ngb] = alt
                    prev[ngb] = node

    return None,None,explored

def getPath(cur,prev):
    fullPath = []
    fullPath.append(cur)
    while cur in prev:
        cur = prev[cur]
        fullPath.append(cur)

    return fullPath

# This heurisic function is admissible, since it never
# overestimates the actual cost. A* is then optimal without
# the explored set (a node might need to be processed more
# than once). However, this is computationally inefficient.
#
# This heuristic function is also monotone/consistent 
# (it is impossible to reduce the distance by adding
# a neighbor to the current path),
# which guarantees that nodes in the explored set 
# cannot have their distance improved, and hence only need
# to be processed once (thus warrant the use of the 
# explored set).
def getHeuristic(u,v):
    # only estimate the true dist
    return np.linalg.norm(np.array(u)-np.array(v))

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

