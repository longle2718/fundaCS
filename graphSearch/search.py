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
    frontierS = []
    frontierS.append(start)
    while len(frontierS) > 0:
        node = frontierS.pop()

        if aMap[node] == 0:
            reachable.append(node)

        explored.append(node)

        # visit neighbors
        for ngb in getNeighbor(node,M,N):
            if ngb not in explored:
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

        # unlike shortest-path probs, each search node should only be 
        # in the queue once. Once enqueued, the node is guaranteed to
        # be visited after a finite amount of time, hence should be marked
        # as explored as soon as it enters the queue.

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
