# Tree traversal using DFS and BFS 
# Unlike graph search probs, each node in a tree 
# does not have overlapping neighbors.
# Hence, there is no need to have the explored queue
# to ensure each node is only visited once.
#
# Long Le <longle1@illinois.edu>
# University of Illinois
#

def dfsPost(root,buf):
    # post-order 
    S = []
    node = root
    nodeLast = None
    # need a stack, a probing node, and a last processed/visited node
    while len(S) > 0 or node != None:
        # at each iteration
        # may process 1 node
        # enqueue/probe all possible nodes
        if node != None:
            S.append(node)
            node = node.left
        else:
            nodePeek = S[-1]
            # if right child exists and node
            # traversed on the left, then 
            # move right
            if nodePeek.right != None and nodeLast != nodePeek.right:
                node = nodePeek.right
            else:
                # at the end
                buf.append(nodePeek.val)
                nodeLast = S.pop()

    return None

def dfsIn(root,buf):
    # in-order
    S = []
    node = root
    # need both the stack and an additional probing node
    while len(S) > 0 or node != None:
        # at each iteration
        # may process 1 node
        # enqueue/probe all possible nodes
        if node != None:
            S.append(node)
            node = node.left
        else:
            node = S.pop()
            buf.append(node.val)
            node = node.right

    return None

def dfsPre(root,buf):
    # pre-order
    if root == None:
        return None

    S = []
    S.append(root)

    while len(S) > 0:
        # at each iteration
        # process 1 node
        # enqueue all possible nodes
        node = S.pop()
    
        buf.append(node.val) 

        if node.right != None:
            S.append(node.right)
        if node.left != None:
            S.append(node.left)

    return None

def bfs(root,buf):
    # also known as level-order
    if root == None:
        return None

    Q = []
    Q.append(root)

    while len(Q) > 0:
        node = Q.pop(0)

        buf.append(node.val)

        if node.left != None:
            Q.append(node.left)
        if node.right != None:
            Q.append(node.right)

    return None

