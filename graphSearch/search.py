# Graph search using DFS and BFS 
# Unlike shortest-path probs, there is no notion of 
# distance in the frontier queue/stack here, i.e. a frontier
# node does not change its priority before being dequeued,
# and hence, should be marked explored as soon as possible.
#
# Long Le <longle1@illinois.edu>
# University of Illinois
#
import numpy as np

def dfs(aMap,start):
    # non recursive implementation
    M,N = np.shape(aMap)
    reachable = []

    explored = []
    frontierS = []
    frontierS.append(start)
    while len(frontierS) > 0:
        node = frontierS.pop()

        if aMap[node] == 0:
            reachable.append(node)

        # visit neighbors
        for ngb in getNeighbor(node,M,N):
            if ngb not in explored:
                explored.append(ngb)

                frontierS.append(ngb)

    return reachable

def bfs(aMap,start):
    M,N = np.shape(aMap)
    reachable = []

    explored = []
    frontierQ = []
    frontierQ.append(start)
    while len(frontierQ) > 0:
        node = frontierQ.pop(0)
        #print('node = '+str(node))

        if aMap[node] == 0:
            reachable.append(node)

        # visit neighbors
        for ngb in getNeighbor(node,M,N):
            if ngb not in explored:
                explored.append(ngb)
                #print('explored = '+str(explored))
                frontierQ.append(ngb)

    return reachable

def getNeighbor(node,M,N):
    ngb = []
    for d in [[0,1],[1,0],[1,1],[0,-1],[-1,0],[-1,-1],[1,-1],[-1,1]]:
        n = tuple(np.array(node)+d) 
        if n[0]>=0 and n[0]<M and n[1]>=0 and n[1]<N:
            ngb.append(n)

    return ngb
