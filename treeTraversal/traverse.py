# Tree traversal using DFS and BFS 
#
# Long Le <longle1@illinois.edu>
# University of Illinois
#

def dfs(root):
    if node == None:
        return None

    #print(node.val) # pre-order
    dfs(root.left)
    #print(node.val) # in-order
    dfs(root.right)
    #print(node.val) # post-order

def bfs(root):
    Q = []
    Q.append(root)
    while len(Q) > 0:
        node = Q.pop(0)

        print(node.val)

        if (node.left != None):
            Q.append(node.left)
        if (node.right != None):
            Q.append(node.right)

