# Tree traversal using DFS and BFS 
# Unlike graph search probs, each node in a tree 
# does not have overlapping neighbors. Hence there is
# no overlapping enqueue. 
# However, for post- and in-order traversal, it is
# possible to re-enqueue processed nodes, which must
# be avoided (completely) by having the explored set 
# to mark processed nodes.
#
# Long Le <longle1@illinois.edu>
# University of Illinois
#

def dfsPost(root,buf):
    # post-order 

    if root == None:
        return None

    S = []
    S.append(root)
    explored = set()
    while len(S) > 0:
        node = S[-1]
        #print('peek = '+str(node.val))

        if ((node.left == None or node.left in explored) and 
            (node.right == None or node.right in explored)):
            buf.append(node.val)
            explored.add(node)
            S.pop()
            #print('pop = '+str(node.val))

        if node.right != None and node.right not in explored:
            S.append(node.right)
        if node.left != None and node.left not in explored:
            S.append(node.left)

    '''
    # Wikipedia implementation
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
            # if right child exists and it's
            # not processed yet, then 
            # move right
            if nodePeek.right != None and nodePeek.right != nodeLast:
                node = nodePeek.right
            else:
                # at the end
                buf.append(nodePeek.val)
                nodeLast = S.pop()
    '''

    return None

def dfsIn(root,buf):
    # in-order

    if root == None:
        return None

    S = []
    S.append(root)
    explored = set() # can be further optimized with just the last node
    while len(S) > 0:
        node = S[-1]
        #print('peek = '+str(node.val))

        if node.left != None and node.left not in explored:
            S.append(node.left)
        else:
            buf.append(node.val)
            explored.add(S.pop())
            #print('pop = '+str(node.val))
            if node.right != None:
                S.append(node.right)

    '''
    # Wikipedia implementation
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
    '''

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

