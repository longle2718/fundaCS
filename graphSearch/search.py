# Graph search using DFS and BFS 
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
    S = []
    S.append(start)
    while len(S) > 0:
        node = S.pop()

        if aMap[node] == 0:
            reachable.append(node)

        explored.append(node)

        # visit neighbors
        for ngb in getNeighbor(node,M,N):
            if ngb not in explored:
                S.append(n)

    return reachable

def bfs(aMap,start):
    M,N = np.shape(aMap)
    reachable = []

    explored = []
    Q = []
    Q.append(start)
    while len(Q) > 0:
        node = Q.pop(0)

        if aMap[node] == 0:
            reachable.append(node)

        explored.append(node)

        # visit neighbors
        for ngb in getNeighbor(node,M,N):
            if ngb not in explored:
                Q.append(n)

    return reachable

def getNeighbor(node,M,N):
    ngb = []
    for d in [[0,1],[1,0],[1,1],[0,-1],[-1,0],[-1,-1],[1,-1],[-1,1]]:
        n = tuple(np.array(node)+d) 
        if n[0]>=0 and n[0]<M and n[1]>=0 and n[1]<N:
            ngb.append(n)

    return ngb
