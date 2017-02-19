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
    def __init__(self,val):
        self.val = val # accumulated edge char
        self.childMap = {} # char to child node map

def buildTrie(words):
    root = TrieNode('$') # required dummy node

    for word in words:
        node = root
        for i in range(len(word)):
            if word[i] not in node.childMap:
                node.childMap[word[i]] = TrieNode(word[:i+1])
            node = node.childMap[word[i]]

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
        
        if len(node.childMap) == 0:
            buf.append(node.val)

        N = len(node.childMap)
        idx = 0
        for _,child in node.childMap.items():
            width = 1/2**(-locMap[node][1]/2)
            if N%2 == 0:
                x = (idx-width/2)*width/(N-1)
                idx += width/(N-1)
            else:
                x = (idx-width/2)*width/N
                idx += width/N

            locMap[child] = tuple(np.array(locMap[node])+np.array((x,-1)))
            #print('child.val,loc = %s,%s' % (child.val,locMap[child]))
            S.append(child)

    if plot:
        plt.figure(figsize=(12, 8), dpi= 80, facecolor='w', edgecolor='k')
        for node,loc in locMap.items():
            #print('node.val,loc = %s,%s' % (node.val,loc))
            plt.annotate(str(node.val),xy=loc,size=18)
            plt.scatter(loc[0],loc[1],lw=32)
            for char,child in node.childMap.items():
                if child in locMap:
                    locChild = locMap[child]
                    #plt.plot([loc[0],locChild[0]],[loc[1],locChild[1]],marker='o',markersize=18)
                    add_arrow(plt.plot([loc[0],locChild[0]],[loc[1],locChild[1]])[0],label=char)
        plt.show()
    
    return buf

def autocomplete(root,word):
    node = root
    for i in range(len(word)):
        if word[i] not in node.childMap:
            break
        else:
            node = node.childMap[word[i]]
    #print('node.val = %s' % node.val)

    return allWords(node)
