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
    serialize_recur(root,buf)
    return ''.join(buf)

def serialize_recur(root,buf):
    if root == None:
        buf.append('X')
        return None

    buf.append(str(root.val))
    serialize_recur(root.left,buf)
    serialize_recur(root.right,buf)
    return None

def deserialize(data):
    return deserialize_recur(list(data))

def deserialize_recur(buf):
    if len(buf) == 0:
        return None
    c = buf.pop(0)
    if c == 'X':
        return None

    root = TreeNode(int(c))
    root.left = deserialize_recur(buf)
    root.right = deserialize_recur(buf)
    return root

def deserializePreIn(preorder, inorder):
    '''
    build a tree using preorder and inorder traversal results
    '''
    N = len(inorder)
    if N == 0:
        return None

    return deserializePreIn_recur(0,0,N-1,preorder,inorder)

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
