# Graph search using DFS and BFS 
# 
# In graph search, there is overlapping enqueue because there is
# overlapping neighbors. To avoid overlapping processing, processed
# nodes need to be kept tracked by the explored set. Note that
# the explored set only helps reduce overlapping enqueues.
#
# Long Le <longle1@illinois.edu>
# University of Illinois
#
import numpy as np

def dfsPre(aMap,start):
    # non recursive implementation
    M,N = np.shape(aMap)
    reachable = []

    explored = set()
    frontierS = []
    frontierS.append(start)
    while len(frontierS) > 0:
        node = frontierS.pop()

        if node in explored:
            continue
        reachable.append(node)
        explored.add(node)

        # visit neighbors
        for ngb in getNeighbor(node,aMap):
            if ngb not in explored:
                frontierS.append(ngb)

    return reachable

def dfsPost(aMap,start):
    # non recursive implementation
    M,N = np.shape(aMap)
    reachable = []

    explored = set()
    frontierS = []
    frontierS.append(start)
    while len(frontierS) > 0:
        node = frontierS[-1]
        #print('peek = '+str(node))

        if node in explored:
            frontierS.pop()
            continue
        ngbs = getNeighbor(node,aMap)
        if len(ngbs) == 0 or allIn(ngbs,explored):
            reachable.append(node)
            explored.add(node)
            frontierS.pop()
            #print('pop = '+str(node))

        # visit neighbors
        for ngb in getNeighbor(node,aMap):
            if ngb not in explored:
                frontierS.append(ngb)

    return reachable

def dfs2Pre(nodes,start):
    # non recursive implementation
    reachable = []

    explored = set()
    frontierS = []
    frontierS.append(start)
    while len(frontierS) > 0:
        node = frontierS.pop()

        if node in explored:
            continue
        reachable.append(node.val)
        explored.add(node)

        # visit neighbors
        for ngb in node.ngbs:
            if ngb not in explored:
                frontierS.append(ngb)

    return reachable

def dfs2Post(nodes,start):
    # non recursive implementation
    reachable = []

    explored = set()
    frontierS = []
    frontierS.append(start)
    while len(frontierS) > 0:
        node = frontierS[-1]
        #print('peek = '+str(node.val))

        if node in explored:
            frontierS.pop()
            continue
        if len(node.ngbs) == 0 or allIn(node.ngbs, explored):
            reachable.append(node.val)
            explored.add(node)
            frontierS.pop()
            #print('pop = '+str(node.val))

        # visit neighbors
        for ngb in node.ngbs:
            if ngb not in explored:
                frontierS.append(ngb)

    return reachable

# Since BFS uses a queue, enqueued nodes are guaranteed to be
# processed in finite steps. Hence overlapping enqueue (and thus
# overlapping processing) can be completely avoided by 
# marking enqueuing (instead of dequeued) nodes as explored.
# Note that this cannot be applied for shortest path problems,
# where priorities/values of nodes in the queue can change
# before being dequeued.
def bfs(aMap,start):
    M,N = np.shape(aMap)
    reachable = []

    explored = set()
    frontierQ = []
    frontierQ.append(start)
    while len(frontierQ) > 0:
        node = frontierQ.pop(0)
        #print('node = '+str(node))

        reachable.append(node)

        # visit neighbors
        for ngb in getNeighbor(node,aMap):
            if ngb not in explored:
                explored.add(ngb)
                #print('explored = '+str(explored))
                frontierQ.append(ngb)

    return reachable

def bfs2(nodes,start):
    reachable = []

    explored = set()
    frontierQ = []
    frontierQ.append(start)
    while len(frontierQ) > 0:
        node = frontierQ.pop(0)
        #print('node = '+str(node))

        reachable.append(node.val)

        # visit neighbors
        for ngb in node.ngbs:
            if ngb not in explored:
                explored.add(ngb)
                #print('explored = '+str(explored))
                frontierQ.append(ngb)

    return reachable

def allIn(nodes,Q):
    for node in nodes:
        if node not in Q:
            return False

    return True

def getNeighbor(node,aMap):
    M,N = np.shape(aMap)
    ngb = []
    for d in [[0,1],[1,0],[1,1],[0,-1],[-1,0],[-1,-1],[1,-1],[-1,1]]:
        n = tuple(np.array(node)+d) 
        if n[0]>=0 and n[0]<M and n[1]>=0 and n[1]<N and aMap[n] == 0:
            ngb.append(n)

    return ngb
