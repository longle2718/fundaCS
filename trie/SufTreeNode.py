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
    root = SufTreeNode('$')

    for word in words:
        node = root

    return root
