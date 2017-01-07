# Tree traversal using DFS and BFS 
# Unlike graph search probs, each node in a tree 
# does not have overlapping neighbors.
# Hence, there is no need to have the explored queue.
#
# Long Le <longle1@illinois.edu>
# University of Illinois
#

def dfs(root,buf):
    if root == None:
        return None

    S = []
    S.append(root)

    while len(S) > 0:
        node = S.pop()
    
        buf.append(node.val) # pre-order

        if (node.right != None):
            S.append(node.right)

        #buf.append(node.val) # in-order

        if (node.left != None):
            S.append(node.left)

        #buf.append(node.val) # post-order

    return None

def bfs(root,buf):
    if root == None:
        return None

    Q = []
    Q.append(root)

    while len(Q) > 0:
        node = Q.pop(0)

        buf.append(node.val)

        if (node.left != None):
            Q.append(node.left)
        if (node.right != None):
            Q.append(node.right)

    return None

