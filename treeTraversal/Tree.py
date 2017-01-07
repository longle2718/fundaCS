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

    S = []
    # create a dummy node 
    root = TreeNode(-1)
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

def deserializePreIn(preorder, inorder):
    '''
    build a tree using preorder and inorder traversal results
    '''
    N = len(inorder)
    if N == 0:
        return None

    root = None
    preStart = 0
    inStart = 0
    inEnd = N-1
    while True:
        if preStart > iEnd:
            break


    return root

def deserializePreIn_recur(preStart,inStart,inEnd,preorder,inorder):
    if preStart > inEnd:
        return None

    root = TreeNode(preorder[preStart])
    inRoot = inorder.index(preorder[preStart])
    if inRoot-1 >= inStart:
        # root of the left subtree is next in preorder
        root.left = deserializePreIn_recur(preStart+1,inStart,inRoot-1,preorder,inorder)
    if inRoot+1 <= inEnd:
        # root of the right subtree is next to preorder + # of nodes in the left subtree
        root.right = deserializePreIn_recur(preStart+inRoot-inStart+1,inRoot+1,inEnd,preorder,inorder)

    return root
