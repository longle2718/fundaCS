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
    locMap = {}
    locMap[root] = (0,0)

    S = []
    S.append(root)
    while len(S) > 0:
        node = S.pop()
        #print('node.val = '+str(node.val))

        if len(buf) > 0:
            c = buf.pop(0)
            #print('c = '+str(c))
            if c != 'X':
                nodeNew = TreeNode(int(c))

                # detect left node
                width = 1/2**(-locMap[node][1])
                if len(S) > 0 and S[-1].val == node.val:
                    node.left = nodeNew

                    locMap[nodeNew] = tuple(np.array(locMap[node])-[width,1])
                else:
                    node.right = nodeNew

                    locMap[nodeNew] = tuple(np.array(locMap[node])-[-width,1])

                S.append(nodeNew)
                S.append(nodeNew)

    if plot:
        del locMap[root]
        for node,loc in locMap.items():
            if node.left in locMap:
                locLeft = locMap[node.left]
                plt.plot([loc[0],locLeft[0]],[loc[1],locLeft[1]],marker='o')
            if node.right in locMap:
                locRight = locMap[node.right]
                plt.plot([loc[0],locRight[0]],[loc[1],locRight[1]],marker='o')
            plt.annotate(str(node.val),xy=loc)
        plt.show()

    # remove the dummy node
    tmp = root
    root = root.right
    del tmp

    return root 

