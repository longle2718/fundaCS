# Tree Node class
#
# Long Le
# University of Illinois
#

import numpy as np
import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def serialize(root):
    buf = []

    S = []
    S.append(root)

    while len(S) > 0:
        node = S.pop()

        if node != None:
            buf.append(str(node.val)+',')

            S.append(node.right)
            S.append(node.left)
        else:
            buf.append('X,')

    return ''.join(buf)

def deserialize(data,plot=False):
    buf = data.split(',')
    del buf[-1]

    # create a dummy node 
    # this is a must in python to update references
    # inside an object due to the lack of pointers
    root = TreeNode(-1)
    S = []
    S.append(root)

    locMap = {}
    locMap[root] = (0,0)
    heightMap = {}
    heightMap[root] = 0

    while len(S) > 0:
        node = S.pop()
        #print('node.val = '+str(node.val))

        if len(buf) > 0:
            c = buf.pop(0)
            #print('c = '+str(c))
            if c != 'X':
                nodeNew = TreeNode(int(c))
                # detect left node
                if len(S) > 0 and S[-1].val == node.val:
                    node.left = nodeNew

                    heightMap[nodeNew] = heightMap[node]+1
                    locMap[nodeNew] = tuple(np.array(locMap[node])-[1/2**heightMap[node],1])
                else:
                    node.right = nodeNew

                    heightMap[nodeNew] = heightMap[node]+1
                    locMap[nodeNew] = tuple(np.array(locMap[node])-[-1/2**heightMap[node],1])

                S.append(nodeNew)
                S.append(nodeNew)

    if plot:
        del locMap[root]
        del heightMap[root]
        for node,loc in locMap.items():
            plt.scatter(loc[0],loc[1])
            plt.annotate(str(node.val),xy=loc)
        plt.show()

    # remove the dummy node
    tmp = root
    root = root.right
    del tmp

    return root 

