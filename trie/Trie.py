# Trie Node class
#
# Long Le
# University of Illinois
#

import numpy as np
import matplotlib.pyplot as plt
import os,sys
sys.path.append(os.path.expanduser('~')+'/randProbs/graphSearch')
from GraphNode import add_arrow

class TrieNode:
    def __init__(self,x):
        self.val = x
        self.children = set()

def findIn(children, val):
    for child in children:
        if child.val == val:
            return child

    return None

def buildTrie(words):
    root = TrieNode('$') # required dummy node

    for word in words:
        node = root
        for i in range(len(word)):
            aChild = findIn(node.children,word[:i+1])
            if aChild == None:
                newNode = TrieNode(word[:i+1])
                node.children.add(newNode)
                node = newNode
            else:
                node = aChild

    return root

def allWords(root,plot=False):
    # get all words from root
    # using preorder-DFS
    buf = []

    locMap = {}
    locMap[root] = (0,0)

    S = []
    S.append(root)
    while len(S) > 0:
        node = S.pop()
        #print('node.val = %s' % node.val)
        
        if len(node.children) == 0:
            buf.append(node.val)

        N = len(node.children)
        idx = 0
        for child in node.children:
            width = 1/2**(-locMap[node][1]/4)
            if N%2 == 0:
                x = (idx-width/2)*width/(N-1)
            else:
                x = (idx-width/2)*width/N
            idx += 1

            locMap[child] = tuple(np.array(locMap[node])+np.array((x,-1)))
            print('child.val,loc = %s,%s' % (child.val,locMap[child]))
            S.append(child)

    if plot:
        plt.figure(figsize=(12, 8), dpi= 80, facecolor='w', edgecolor='k')
        for node,loc in locMap.items():
            #print('node.val,loc = %s,%s' % (node.val,loc))
            plt.annotate(str(node.val),xy=loc,size=18)
            plt.scatter(loc[0],loc[1],lw=32)
            for child in node.children:
                if child in locMap:
                    locChild = locMap[child]
                    #plt.plot([loc[0],locChild[0]],[loc[1],locChild[1]],marker='o',markersize=18)
                    add_arrow(plt.plot([loc[0],locChild[0]],[loc[1],locChild[1]])[0])
        plt.show()
    
    return buf

def autocomplete(root,word):
    prefix = []
    node = root
    for c in word:
        # find vertically
        if node.val == c:
            node = node.child
        else:
            # find horizontally
            tmp = node
            while tmp!= None:
                if tmp.val == c:
                    node = tmp
                    break
                tmp = tmp.next

            # form the result
            rv = []
            for postfix in allWords(node):
                rv.append(word+postfix[1:])
            return rv

    return word
