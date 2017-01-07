# Tree Node class
#
# Long Le
# University of Illinois
#

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
            buf.append(str(node.val))

            S.append(node.right)
            S.append(node.left)
        else:
            buf.append('X')

    return ''.join(buf)

def deserialize(data):
    buf = list(data)

    # create a dummy node 
    # this is a must in python to update references
    # inside an object due to the lack of pointers
    root = TreeNode(-1)
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
                if len(S) > 0 and S[-1].val == node.val:
                    node.left = nodeNew
                else:
                    node.right = nodeNew

                S.append(nodeNew)
                S.append(nodeNew)

    # remove the dummy node
    tmp = root
    root = root.right
    del tmp

    return root 

