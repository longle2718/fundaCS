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

def buildTree(preorder, inorder):
    '''
    build a tree using preorder and inorder traversal results
    '''
    N = len(inorder)
    if N == 0:
        return None

    return recur(0,0,N-1,preorder,inorder)

def buildTree_recur(preStart,inStart,inEnd,preorder,inorder):
    root = TreeNode(preorder[preStart])
    inRoot = inorder.index(preorder[preStart])
    if inRoot-1 >= inStart:
        # root of the left subtree is next in preorder
        root.left = buildTree_recur(preStart+1,inStart,inRoot-1,preorder,inorder)
    if inRoot+1 <= inEnd:
        # root of the right subtree is next to preorder + # of nodes in the left subtree
        root.right = buildTree_recur(preStart+inRoot-inStart+1,inRoot+1,inEnd,preorder,inorder)

    return root
