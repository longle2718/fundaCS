# Suffix Tree Node class
#
# Long Le
# University of Illinois
#

import numpy as np
import matplotlib.pyplot as plt
import os,sys
sys.path.append(os.path.expanduser('~')+'/randProbs/graphSearch')
sys.path.append('../graphSearch')
from GraphNode import add_arrow

class SufTreeNode:
    def __init__(self,val):
        self.val = val # accumulated edge char
        self.childMap = {} # char to child node map

# First suffix tree construction algorithm in O(n)
# is by McCreight.
#
# For online construction, there is Ukkonen algorithm with 
# O(n) for constant-size alphabet, and
# the worst case of O(nlogn) for general alphabet.
#
# For O(n) in general alphabet, there is Farach algorithm.
#
def buildSufTree(words):
    # using McCreight ideas
    # Reference:
    # [1] http://wind.in.tum.de/seminare/textalgo/WS0203/Izamski.pdf
    # [2] http://users-birc.au.dk/cstorm/courses/StrAlg_f12/slides/suffix-tree-construction.pdf
    root = SufTreeNode('$')
    head = ''

    for word in words:
        for k in range(len(word)-1):
            suf = word[k:]
            print('suf = %s' % suf)
            for sufEdge,child in root.childMap.items():
                head = getHead(suf,sufEdge)
                if  head == '':
                    continue
                else:
                    break

            print('head = %s' % head)
            if head == '':
                root.childMap[suf] = SufTreeNode(suf)
            else:
                tail = getTail(suf,head)
                depthIter(head,tail,sufEdge,root)

    return root

def getHead(sufi,sufj,sIdx=0):
    # get head, i.e. the longest prefix, of sufi
    #print('sufi = %s, sufj = %s' % (sufi,sufj))
    if sufi[sIdx] != sufj[sIdx]:
        return ''

    rv = sufi[sIdx]
    for k in range(sIdx+1,min(len(sufi),len(sufj))):
        if sufi[k] != sufj[k]:
            break
        else:
            rv += sufi[k]
    return rv

def getTail(suf,head):
    return suf[len(head):]

def depthIter(head,tail,sufEdge,node):
    d = len(sufEdge) # depth
    while len(head) > d:
        # updated node and sufEdge while exploring depth
        node = node.childMap[sufEdge]
        for sufEdge,child in node.childMap.items():
            headNew = getHead(head,sufEdge,d)
            if len(headNew) == d:
                continue
            else:
                d += len(sufEdge)
                break

    if len(head) < d:
        # insert node here
        savedNode = node.childMap[sufEdge]
        del node.childMap[sufEdge]

        node.childMap[head] = SufTreeNode(head)
        node.childMap[head].childMap[getTail(savedNode.val,head)] = savedNode
        node.childMap[head].childMap[tail] = SufTreeNode(head+tail)

    return 

