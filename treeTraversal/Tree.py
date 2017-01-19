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
    parentMap = {}
    parentMap[root] = None

    while len(S) > 0:
        node = S.pop()
        #print('node.val = '+str(node.val))

        if len(buf) > 0:
            c = buf.pop(0)
            #print('c = '+str(c))
            if c != 'X':
                nodeNew = TreeNode(int(c))

                parentMap[nodeNew] = node
                heightMap[nodeNew] = heightMap[node]+1

                # detect left node
                if len(S) > 0 and S[-1].val == node.val:
                    node.left = nodeNew

                    locMap[nodeNew] = tuple(np.array(locMap[node])-[1/2**heightMap[node],1])
                else:
                    node.right = nodeNew

                    locMap[nodeNew] = tuple(np.array(locMap[node])-[-1/2**heightMap[node],1])

                S.append(nodeNew)
                S.append(nodeNew)

    if plot:
        del locMap[root]
        del heightMap[root]
        del parentMap[root]
        for node,loc in locMap.items():
            if parentMap[node] in locMap:
                locParent = locMap[parentMap[node]]
                plt.plot([locParent[0],loc[0]],[locParent[1],loc[1]],marker='o')
            plt.annotate(str(node.val),xy=loc)
        plt.show()

    # remove the dummy node
    tmp = root
    root = root.right
    del tmp

    return root 

